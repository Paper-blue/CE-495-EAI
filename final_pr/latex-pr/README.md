# Academic LaTeX Beamer Presentation System

## 📋 File Overview

### Core Files
- `energy_aware_ai_presentation.tex` - Main English LaTeX beamer document (Academic style)
- `presentation_reference_chinese.md` - Chinese reference guide for presentation content
- `compile.bat` - Windows compilation script
- `README.md` - This documentation

## 🎯 Presentation Design

### Academic Style Features
- **Professional Madrid theme** with academic color scheme
- **Times New Roman** for main text, **Arial** for sans-serif
- **Formal academic language** throughout
- **Clean layout** without decorative elements
- **Structured content** following academic presentation standards

### Presentation Structure (12 slides, 7 minutes)
| Slide | Content | Duration | Purpose |
|-------|---------|----------|---------|
| 1 | Title Page | 10s | Project introduction |
| 2-3 | Motivation + Research Question | 50s | Problem statement |
| 4-6 | Methodology + Metrics + Setup | 90s | Research approach |
| 7-9 | Three Key Findings | 180s | Main results |
| 10-11 | Deployment Guidelines | 60s | Practical value |
| 12 | Contributions & Impact | 30s | Conclusion |

### Key Features
- **English presentation** with academic terminology
- **Precise data presentation** (25%, 40%, 1,287,000 kWh, etc.)
- **Professional color coding**:
  - Academic Blue: Main structure
  - Highlight Red: Key findings
  - Success Green: Positive results
- **Mathematical formulas** for EOR and TWEOR metrics
- **Comprehensive tables** for quantization and deployment analysis

## 🚀 Quick Start

### 1. Environment Setup

**Requirements**:
- [TeX Live](https://www.tug.org/texlive/) or [MiKTeX](https://miktex.org/)
- XeLaTeX compiler
- Standard academic fonts (Times New Roman, Arial)

**Verification**:
```cmd
xelatex --version
```

### 2. Compilation

**Method 1: Using Batch Script (Recommended)**
```cmd
# Double-click compile.bat
# Or run in command line:
.\compile.bat
```

**Method 2: Manual Compilation**
```cmd
xelatex energy_aware_ai_presentation.tex
xelatex energy_aware_ai_presentation.tex
```

**Method 3: VS Code LaTeX Workshop**
- The file includes `% !TEX program = xelatex` directive
- Use Ctrl+Alt+B or click compile button

### 3. Output
- `energy_aware_ai_presentation.pdf` - Final academic presentation slides

## 📊 Content Overview

### Research Focus
**"Energy-Aware AI Deployment: Investigating the Interplay of Model Quantization and Hardware Platforms"**

### Key Research Contributions
1. **First quantization-hardware co-optimization framework**
2. **Novel EOR/TWEOR energy efficiency metrics**
3. **Evidence-based deployment guidelines**

### Major Findings
- **25%** energy reduction through INT8 quantization
- **40%** overall efficiency improvement through synergistic optimization
- **98%+** accuracy preservation across all methods

### Practical Impact
- **Deployment matrix** for different use cases
- **Scientific decision framework** balancing performance, efficiency, and cost
- **Hardware-software co-optimization** guidelines

## 🎨 Academic Design Elements

### Color Scheme
```latex
Academic Blue: RGB(0,51,102)    - Structure and emphasis
Highlight Red: RGB(153,0,0)     - Key findings and alerts
Success Green: RGB(0,102,51)    - Positive results
Academic Gray: RGB(64,64,64)    - Secondary text
```

### Typography
- **Main font**: Times New Roman (academic standard)
- **Sans-serif**: Arial (clean presentation text)
- **Math formulas**: Computer Modern (LaTeX default)

### Layout Principles
- **Clean and professional** appearance
- **Consistent spacing** and alignment
- **Logical information hierarchy**
- **Balanced text-to-visual ratio**

## 🔧 Customization Guide

### Modifying Content
1. Open `energy_aware_ai_presentation.tex`
2. Locate the relevant `\begin{frame}` block
3. Edit content while maintaining structure
4. Recompile

### Custom Commands
```latex
\highlight{text}    % Red highlighting for key points
\success{text}      % Green highlighting for positive results
\emphasis{text}     % Blue highlighting for structural emphasis
```

### Adding Slides
```latex
%% New Slide: Title (timing)
\begin{frame}
\frametitle{Your Title Here}
% Your content
\end{frame}
```

## 📈 Presentation Guidelines

### Time Management Strategy
- **Introduction** (1 min): Quick context and problem statement
- **Methodology** (1.5 min): Systematic approach presentation
- **Results** (3 min): Focus on three key findings with data
- **Applications** (1 min): Practical deployment value
- **Conclusion** (0.5 min): Concise impact summary

### Delivery Tips
1. **Emphasize key numbers** with gestures (25%, 40%, 98%+)
2. **Pause at "synergistic optimization"** for impact
3. **Use confident tone** in conclusion
4. **Prepare for technical questions** about methodology

### Visual Presentation
- **Point to specific data** in tables
- **Use laser pointer** for formula components
- **Maintain eye contact** during key findings
- **Gesture toward graphs** when explaining trends

## 🔍 Troubleshooting

### Common Issues

**Compilation Error**:
```
! LaTeX Error: File `fontspec.sty' not found.
```
**Solution**: Install fontspec package
```cmd
tlmgr install fontspec
```

**Font Issues**:
```
Font "Times New Roman" not found
```
**Solution**: 
- Ensure Times New Roman is installed on system
- Alternative: Use `\setmainfont{TeX Gyre Termes}` (TeX Live included)

**XeLaTeX Required**:
```
! Package fontspec Error: The fontspec package requires either XeTeX or LuaTeX.
```
**Solution**: Ensure using XeLaTeX compiler, not pdfLaTeX

### Environment Check
```cmd
# Check required packages
kpsewhich fontspec.sty
kpsewhich beamer.cls
kpsewhich booktabs.sty
```

## 📝 Advanced Features

### Adding Graphics
```latex
\begin{figure}
\centering
\includegraphics[width=0.8\textwidth]{your-image.pdf}
\caption{Your caption here}
\end{figure}
```

### TikZ Diagrams
```latex
\begin{tikzpicture}
\draw[fill=academicblue!20] (0,0) rectangle (4,2);
\node at (2,1) {Your content};
\end{tikzpicture}
```

### Animation Effects
```latex
\only<2->{Content appears on click 2}
\alert<3>{Content highlighted on click 3}
```

## 🎯 Final Checklist

Before presentation:
- [ ] PDF generated successfully
- [ ] All numbers display correctly (25%, 40%, 1,287,000)
- [ ] Fonts render properly
- [ ] Tables are well-formatted
- [ ] Color contrast is clear
- [ ] Total slides: 12 + 1 Q&A backup
- [ ] Timing: ~7 minutes total
- [ ] Backup questions prepared

## 📞 Support

**Technical Issues**: Check LaTeX installation and package availability
**Content Questions**: Refer to `presentation_reference_chinese.md` for detailed Chinese explanations
**Last Updated**: January 2025

---

## 🌟 Quick Reference: Key Messages

### Opening (Slides 1-3)
> "Today we present a systematic approach to energy-efficient LLM deployment through quantization-hardware co-optimization, addressing a critical gap in inference-stage energy optimization."

### Methodology (Slides 4-6)
> "Our three-pillar approach combines quantization analysis, hardware evaluation, and novel energy metrics, enabling systematic evaluation across 6 platforms, 6 models, and 5 benchmark tasks."

### Key Findings (Slides 7-9)
> "We achieved three major findings: 25% energy reduction through INT8 quantization, 20-30% efficiency gains from Ada Lovelace architecture, and 40% overall improvement through synergistic optimization."

### Practical Value (Slides 10-12)
> "Our research provides evidence-based deployment guidelines, from data center production using A100+INT8 to edge computing with RTX 4060Ti+dynamic quantization, establishing a scientific framework for sustainable AI development." 