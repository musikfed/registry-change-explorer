@echo off
setlocal
cd /d "%~dp0"
set RCE_DEMO_MODE=1

if not exist .venv (
  py -3 -m venv .venv
)
call .venv\Scripts\activate
python -m pip install -r requirements.txt
python run.py
