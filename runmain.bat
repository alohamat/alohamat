@echo off
setlocal enabledelayedexpansion

set filename=main

:inicio
cls
echo ============================
echo == INDIAN BOXER C++ RUNNER ==
echo ============================

:: Compila
g++ "%filename%.cpp" -o "%filename%.exe"
if %errorlevel% neq 0 (
    echo ERRO NA COMPILACAO, DESGRAÇA!
    pause
    goto fim
)
echo Compilado com sucesso!

:: Executa automaticamente
echo.
echo Executando automaticamente...
echo ----------------------------
"%filename%.exe"
echo.
pause

:menu
echo.
echo E AGORA, BRABO?
echo [1] Rodar de novo
echo [2] Compilar de novo
echo [3] Sair
set /p choice=Escolha: 

if "%choice%"=="1" (
    echo Executando...
    echo ----------------------------
    "%filename%.exe"
    echo.
    pause
    goto menu
) else if "%choice%"=="2" (
    goto inicio
) else if "%choice%"=="3" (
    goto fim
) else (
    echo Opcao invalida, CORNO! Tenta de novo!
    pause
    goto menu
)

:fim
if exist "%filename%.exe" (
    echo Limpando sujeira...
    del "%filename%.exe"
)
echo Falou, LENDA!
timeout /t 1 >nul
exit
