<div align="center">
  <div>&nbsp;</div>
  <img src="resources/openvoicelogo.jpg" width="400"/> 

[Paper](https://arxiv.org/abs/2312.01479) |
[Website](https://research.myshell.ai/open-voice) 

</div>

## Original
OpenVoice : https://github.com/myshell-ai/OpenVoice

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/VYNCX/OpenVoice-WebUI.git
   cd OpenVoice-WebUI
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
  for GPU usage : 
  ```bash 
  python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```

  Download model [download](https://github.com/VYNCX/OpenVoice-WebUI/releases/download/Download/OPENVOICE_MODELS.zip) and extract in OPENVOICE_MODELS . 
  
4. Run WebUI:
   ```bash
   python openvoice_webui.py
   ```
