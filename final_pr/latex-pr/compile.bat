@echo off
echo ========================================
echo Compiling Academic LaTeX Beamer Presentation
echo ========================================

:: Check if XeLaTeX is installed
where xelatex >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: XeLaTeX not found. Please install TeX Live or MiKTeX.
    pause
    exit /b 1
)

:: Compile LaTeX document (requires two runs for proper cross-references)
echo Compiling presentation with XeLaTeX...
xelatex -interaction=nonstopmode energy_aware_ai_presentation.tex
if %errorlevel% neq 0 (
    echo First compilation failed! Please check LaTeX code.
    pause
    exit /b 1
)

echo Second compilation...
xelatex -interaction=nonstopmode energy_aware_ai_presentation.tex
if %errorlevel% neq 0 (
    echo Second compilation failed! Please check LaTeX code.
    pause
    exit /b 1
)

:: Clean temporary files
echo Cleaning temporary files...
del *.aux *.log *.nav *.out *.snm *.toc *.vrb *.fls *.fdb_latexmk 2>nul

echo ========================================
echo Compilation completed! Generated: energy_aware_ai_presentation.pdf
echo ========================================

:: Try to open PDF file
if exist energy_aware_ai_presentation.pdf (
    echo Opening PDF file...
    start energy_aware_ai_presentation.pdf
) else (
    echo Warning: PDF file not found.
)

pause 