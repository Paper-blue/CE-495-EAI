@echo off
:: Quick compilation script for ACM report
:: For testing and quick iterations

echo Quick compiling ACM report...

set MAIN_FILE=energy_aware_ai_deployment_acm

:: Single compilation (for quick testing)
pdflatex -interaction=nonstopmode %MAIN_FILE%.tex > nul 2>&1

if exist "%MAIN_FILE%.pdf" (
    echo Success! PDF generated.
    start "" "%MAIN_FILE%.pdf"
) else (
    echo Compilation failed. Use compile_acm.bat for detailed output.
    pause
)

:: Clean up
del /f /q *.aux *.log 2>nul 