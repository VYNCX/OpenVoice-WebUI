import os
import torch
import gradio as gr
from openvoice import se_extractor
from openvoice.api import ToneColorConverter

# Output directory setup
output_dir = './openvoice_outputs'
os.makedirs(output_dir, exist_ok=True)

# Gradio function
def voice_cloning(base_speaker, reference_speaker, model_version, device_choice):
    try:
        # Determine paths and device
        ckpt_converter = f'./OPENVOICE_MODELS/{model_version}'
        device = "cuda:0" if device_choice == "GPU" and torch.cuda.is_available() else "cpu"
        print(f"Device: {device}")
        
        # Load the ToneColorConverter
        tone_color_converter = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
        tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

        # Extract speaker embeddings
        source_se, _ = se_extractor.get_se(base_speaker, tone_color_converter, vad=False)
        target_se, _ = se_extractor.get_se(reference_speaker, tone_color_converter, vad=False)
        
        # Define output file paths
        save_path = f'{output_dir}/output_cloned.wav'
        
        # Perform tone color conversion
        tone_color_converter.convert(
            audio_src_path=base_speaker, 
            src_se=source_se, 
            tgt_se=target_se, 
            output_path=save_path,
        )
        return save_path, "Voice cloning successful!"
    except Exception as e:
        return None, f"Error: {str(e)}"

# Gradio UI setup
with gr.Blocks(theme=gr.themes.Monochrome()) as ui:
    gr.Markdown("# 🎤 Voice Cloning with OpenVoice")
    gr.Markdown("Clone a voice by uploading a **Base Speaker** and a **Reference Speaker**. Customize model version and device settings.")
    
    with gr.Row():
        base_speaker_input = gr.Audio(label="Base Speaker (Source Voice)", type="filepath")
        reference_speaker_input = gr.Audio(label="Reference Speaker (Target Voice)", type="filepath")
    
    with gr.Row():
        model_version = gr.Dropdown(
            ["v1", "v2"], 
            value="v2", 
            label="Model Version"
        )
        device_choice = gr.Dropdown(
            ["CPU", "GPU"], 
            value="GPU" if torch.cuda.is_available() else "CPU", 
            label="Device"
        )
    
    with gr.Row():
        clone_button = gr.Button("Clone Voice")
    
    output_audio = gr.Audio(label="Cloned Voice", type="filepath", interactive=False)
    status_output = gr.Textbox(label="Status", interactive=False)
    
    # Set up the cloning process
    def handle_clone(base_speaker, reference_speaker, model_version, device_choice):
        result, status = voice_cloning(base_speaker, reference_speaker, model_version, device_choice)
        return result, status
    
    clone_button.click(
        handle_clone,
        inputs=[base_speaker_input, reference_speaker_input, model_version, device_choice],
        outputs=[output_audio, status_output],
    )

ui.launch(inbrowser=True)
