# CE 495 EAI Final Project Presentation Script
## Total Time: 7 Minutes

---

## Slide 1: Title Page (10 seconds)
**Time: 0:00-0:10**

Hello everyone. I am [Your Name]. Today I will show you our team's final project for CE 495 Energy-Aware Intelligence course. Our research title is "Towards Energy-Aware AI Deployment: Investigating the Interplay of Model Quantization and Hardware Platforms." This is a team project with three members. We focus on quantization techniques, hardware evaluation, and energy metrics.

---

## Slide 2: Research Motivation (25 seconds)
**Time: 0:10-0:35**

Let me start with why this research matters. Training one large Transformer model uses about **1.3 million kilowatt-hours** of electricity. This equals the lifetime carbon emissions of several cars. While training energy gets a lot of attention, inference energy does not get enough focus. But inference happens much more often in real applications. As you can see in the chart, inference energy adds up to be very significant. This is why we focus on **inference-stage energy optimization**.

---

## Slide 3: Core Research Question (25 seconds)  
**Time: 0:35-1:00**

Our main research question is: **How can we achieve energy-efficient LLM deployment through systematic optimization of quantization techniques and hardware platforms?**

Current research has three main problems. First, most studies look at single optimization factors. Second, there are no systematic evaluation frameworks. Third, there is limited practical deployment guidance.

Our contributions include: a systematic co-optimization approach, a comprehensive evaluation framework, and practical deployment guidelines. We will show you how to reduce energy use while keeping model performance.

---

## Slide 4: Methodology Overview (30 seconds)
**Time: 1:00-1:30**

We use a three-pillar research approach.

**Pillar 1 is Quantization Analysis**: We test INT8, FP16, and dynamic quantization. We study performance-energy trade-offs and memory optimization.

**Pillar 2 is Hardware Evaluation**: We test 6 GPU platforms across 3 hardware generations. We do comprehensive energy profiling.

**Pillar 3 is Energy Metrics**: We develop new EOR and TWEOR metrics. We use 1Hz precision monitoring for deployment optimization.

This creates a **systematic co-optimization framework: 6 platforms × 6 models × 5 tasks**.

---

## Slide 5: Novel Energy Efficiency Metrics (30 seconds)
**Time: 1:30-2:00**

We develop two key energy efficiency metrics.

**EOR (Energy Output Ratio)** equals performance score divided by energy consumption in watt-hours. This metric shows how much performance you get per unit of energy.

**TWEOR (Time-Weighted Energy Output Ratio)** also includes inference time for complete efficiency evaluation.

These metrics have three advantages: they capture complex trade-offs, they include time efficiency, and they enable deployment optimization. We use NVIDIA SMI with 1Hz sampling rate for precise energy measurements.

---

## Slide 6: Experimental Setup (30 seconds)
**Time: 2:00-2:30**

Our experimental setup is very comprehensive.

For hardware, we test 6 GPU platforms: A100, RTX 4090, 3090Ti, 4060Ti, V100, and L40S. For models, we choose 6 representative language models: Qwen2.5, DeepSeek-R1, Mistral, Neural-Chat, Bloomz, and Yi. For quantization, we test INT8, FP16, and dynamic quantization.

Our benchmark tasks include 5 important tests: MMLU for multi-task language understanding, HellaSwag for common sense reasoning, ARC for science questions, TruthfulQA for truthfulness evaluation, and GSM8K for math reasoning.

This creates a **comprehensive evaluation: 6 platforms × 6 models × 5 benchmark tasks**.

---

## Slide 7: Finding 1 - Quantization Impact (60 seconds)
**Time: 2:30-3:30**

Now let's look at our first important finding: quantization technique effectiveness.

The table shows that **INT8 quantization** performs best. Compared to the FP32 baseline, it achieves **25% energy reduction** with less than 1% accuracy loss. EOR improvement reaches **32.1%** with an excellent rating. FP16 mixed precision achieves 16.3% energy reduction compared to FP32 baseline with only 0.2% accuracy loss. Dynamic quantization has moderate effects with 10.5% energy reduction.

For example, with DeepSeek-7B model, INT8 quantization reduces energy from **39.65 watt-hours** (FP32 baseline) **to 29.74 watt-hours**. Accuracy drops only 0.7 to 0.9 percentage points. This works because of reduced memory bandwidth needs and optimized integer arithmetic on modern GPUs.

The chart on the right shows quantization trade-offs. INT8 quantization finds the best balance between energy and performance. This proves that INT8 quantization is the most practical quantization strategy.

---

## Slide 8: Finding 2a - A100 Leadership (30 seconds)
**Time: 3:30-4:00**

Our second finding is about hardware platforms. **A100 PCIE is clearly the energy efficiency champion**.

A100 technical specs include 1,555 GB/s memory bandwidth, 3rd generation Tensor Cores, 40GB HBM2 memory, and advanced Ampere architecture.

For performance, A100 achieves the **highest energy efficiency** in all scenarios. It is optimized for AI workloads. It has superior memory bandwidth utilization and enterprise-grade reliability.

Most importantly, A100 **leads in EOR and TWEOR metrics across all benchmark tasks**. This proves its absolute advantage in energy efficiency.

---

## Slide 9: Finding 2b - Platform Analysis (30 seconds)
**Time: 4:00-4:30**

Further platform analysis shows we can group GPU platforms into three categories: **High bandwidth platforms** like A100 and V100, **Power optimized platforms** like RTX 4060Ti, and **High performance platforms** like RTX 4090.

**Ada Lovelace architecture** achieves **20-30% energy efficiency improvement** compared to the previous Turing architecture generation. This shows how hardware evolution impacts energy efficiency.

The performance heatmap on the right visually shows different platform performance across metrics. A100 shows the deepest colors in most metrics, indicating its superior performance.

---

## Slide 10: Finding 3 - Synergistic Optimization (60 seconds)
**Time: 4:30-5:30**

Our third and most important finding is synergistic optimization effects. **A100 PCIE with INT8 quantization achieves 40% overall energy efficiency improvement** compared to a baseline configuration.

The table shows A100+INT8 combination reaches **40.0%** EOR efficiency gain compared to baseline. RTX 4090+FP16 combination reaches **35.2%**. RTX 4060Ti+Dynamic combination reaches 25.1%.

Beyond hardware-software co-optimization, we also find **knowledge distillation** provides an additional **19.8% energy reduction** compared to standard models while maintaining **98%+ accuracy**.

The key insight is: **Hardware-software co-optimization enables multiplicative benefits**. Using quantization alone or efficient hardware alone has limited effects. But combining both creates synergistic effects that go beyond simple addition.

---

## Slide 11: Deployment Decision Flow (30 seconds)
**Time: 5:30-6:00**

Based on our research results, we design a systematic deployment decision flow.

The decision process starts with **deployment requirements assessment**. First, determine available hardware resources. If A100 is available, consider accuracy needs: **High accuracy needs choose A100+FP16, energy priority chooses A100+INT8**.

If using RTX series GPUs, consider energy priority: **Performance priority chooses RTX 4090+FP16, energy priority chooses RTX 4060Ti+Dynamic**.

This decision flow follows **Assessment → Analysis → Consideration → Optimization** systematic process. This ensures finding optimal configurations in different scenarios.

---

## Slide 12: Deployment Decision Matrix (30 seconds)
**Time: 6:00-6:30**

We further specify the decision flow into a deployment decision matrix.

For different use cases, we provide specific recommended configurations:

**Data Center Production**: A100 PCIE + INT8 quantization, 98% performance, **40%** efficiency gain, high cost but maximum benefit.

**Enterprise Applications**: RTX 4090 + FP16, 99% performance, **35%** efficiency gain, medium cost.

**Edge Computing**: RTX 4060Ti + Dynamic quantization, 95% performance, 25% efficiency gain, lowest cost.

Selection principles are: **Accuracy priority chooses FP16 mixed precision, energy priority chooses INT8 quantization, flexibility priority chooses dynamic quantization**. This matrix provides clear guidance for actual deployment.

---

## Slide 13: Application Guidelines (30 seconds)
**Time: 6:30-7:00**

Finally, we provide specific application guidelines for three typical deployment scenarios.

**Data Center Production**: Use A100 PCIE + INT8 quantization, suitable for high throughput and controlled environments, 98% performance, **40%** efficiency improvement.

**Enterprise Applications**: Use RTX 4090 + FP16 mixed precision, balances cost and performance, 99% performance, **35%** efficiency improvement.

**Edge Computing Deployment**: Use RTX 4060 Ti + Dynamic quantization, adapts to power constraints and compact space, 95% performance, **25%** efficiency improvement.

These **customized recommendations for different deployment scenarios and operational requirements** provide directly usable guidance for practical applications.

---

## Slide 14: Research Contributions and Impact (30 seconds)
**Time: 7:00-7:30**

To summarize our key contributions: First is the quantization-hardware co-optimization framework. Second is novel EOR/TWEOR energy efficiency metrics. Third is evidence-based deployment guidelines.

Our **key results** include: **25% energy reduction**, **40% co-optimization gains**, and **98%+ accuracy preservation**.

This research provides systematic solutions for energy-aware AI deployment. It has important significance for promoting green AI technology development.

**Thank you for your attention!**

---

## Presentation Summary

### Time Allocation:
- Opening Introduction: 1 minute (Slides 1-3)
- Methodology: 1.5 minutes (Slides 4-6)
- Research Findings: 3 minutes (Slides 7-10)
- Application Guidelines: 1 minute (Slides 11-13)
- Summary: 0.5 minutes (Slide 14)

### Key Data to Emphasize:
- **1,287,000 kWh** - Large model training energy
- **25%** - INT8 quantization energy reduction
- **40%** - Co-optimization efficiency improvement  
- **98%+** - Accuracy preservation

### Speaking Tips:
1. Control speed to 150-170 words per minute
2. Pause before key data for emphasis
3. Use hand gestures to point to relevant charts
4. Keep confident tone with appropriate pauses
5. Emphasize important findings with stronger voice

### Simple Vocabulary Used:
- "achieves" instead of "accomplishes"
- "shows" instead of "demonstrates"
- "uses" instead of "utilizes"
- "gets" instead of "obtains"
- "works" instead of "functions"

### Baseline References for Energy Reductions:
- **25% quantization energy reduction**: Compared to FP32 (32-bit floating point) baseline
- **40% co-optimization efficiency gain**: Compared to baseline configuration EOR metrics
- **20-30% hardware improvement**: Ada Lovelace vs previous Turing architecture
- **19.8% knowledge distillation reduction**: Compared to standard (non-distilled) models 