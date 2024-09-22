@echo off
if not exist "installed.flag" (
    echo Instalando dependências do requirements.txt...
    python -m pip install -r "C:\Users\Pichau\Documents\Projetos\downloader\requirements.txt"
    
    echo Dependências instaladas > installed.flag
) else (
    echo Dependências já instaladas, pulando instalação...
)
python "C:\Users\Pichau\Documents\Projetos\downloader\app.py"

pause
