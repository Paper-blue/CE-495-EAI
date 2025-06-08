@echo off
echo Compiling Energy-Aware AI Deployment ACM Report...
echo.

:: Set the main LaTeX file name
set MAIN_FILE=energy_aware_ai_deployment_acm

:: First compilation
echo [1/4] First pdflatex compilation...
pdflatex -interaction=nonstopmode %MAIN_FILE%.tex
if %errorlevel% neq 0 (
    echo Error in first compilation!
    pause
    exit /b 1
)

:: BibTeX compilation
echo [2/4] BibTeX compilation...
bibtex %MAIN_FILE%
if %errorlevel% neq 0 (
    echo Warning: BibTeX compilation had issues, continuing...
)

:: Second compilation
echo [3/4] Second pdflatex compilation...
pdflatex -interaction=nonstopmode %MAIN_FILE%.tex
if %errorlevel% neq 0 (
    echo Error in second compilation!
    pause
    exit /b 1
)

:: Third compilation (final)
echo [4/4] Final pdflatex compilation...
pdflatex -interaction=nonstopmode %MAIN_FILE%.tex
if %errorlevel% neq 0 (
    echo Error in final compilation!
    pause
    exit /b 1
)

:: Clean up auxiliary files
echo.
echo Cleaning up auxiliary files...
del /f /q *.aux *.log *.bbl *.blg *.toc *.out *.fdb_latexmk *.fls *.synctex.gz 2>nul

echo.
echo ======================================
echo Compilation completed successfully!
echo Output: %MAIN_FILE%.pdf
echo ======================================
echo.

:: Open the PDF if it exists
if exist "%MAIN_FILE%.pdf" (
    echo Opening PDF...
    start "" "%MAIN_FILE%.pdf"
) else (
    echo Warning: PDF file not found!
)

pause 