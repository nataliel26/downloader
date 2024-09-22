@echo off
if not exist "installed.flag" (
    echo Instalando dependências do requirements.txt...
    python -m pip install -r "your-path\requirements.txt"
    
    echo Dependências instaladas > installed.flag
) else (
    echo Dependências já instaladas, pulando instalação...
)
python "your-path\app.py"

pause
