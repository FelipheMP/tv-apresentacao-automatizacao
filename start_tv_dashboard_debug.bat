@echo off

:: Entra na pasta onde este arquivo .bat está localizado
cd /d "%~dp0"

:: Ativa o ambiente virtual do Python
call .venv\Scripts\activate.bat

:: Executa a automação
python main.py

:: Mantém a janela aberta, exibindo erros que possam ocorrer durante a inicialização do .bat
pause
