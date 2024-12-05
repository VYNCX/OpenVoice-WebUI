@echo off

set "current_dir=%CD%"
call "%current_dir%\venv\Scripts\activate.bat"
python "%current_dir%\openvoice_webui.py"

pause