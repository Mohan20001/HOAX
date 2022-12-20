@echo off
pip install pyngrok
pip install pyfiglet
pip install colorama
@REM ngrok config add-authtoken 299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf //
set /p a=authtoken : 
ngrok config add-authtoken %a%
echo %a% > ngrok_api_log.txt
@REM 299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf //
pause
python run.py
