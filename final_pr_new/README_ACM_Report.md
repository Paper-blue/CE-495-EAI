# Energy-Aware AI Deployment: ACM格式最终报告

## 项目概述

本报告按照ACM Sigconf模板格式化，满足CE 495 Energy-Aware Intelligence课程的最终项目要求。

**研究主题**: 面向能源感知的AI部署：模型量化与硬件平台互动关系研究

**团队成员**:
- 边昊济 (haojibian2027@u.northwestern.edu) - 量化技术研究
- 王子楠 (zinanwang2027@u.northwestern.edu) - 硬件平台评估  
- 吕任远 (renyuanlu2027@u.northwestern.edu) - 能源效率指标开发

---

## 文件结构

```
final_pr_new/
├── energy_aware_ai_deployment_acm.tex    # 主要报告文件 (ACM格式)
├── compile_acm.bat                       # Windows编译脚本
├── README_ACM_Report.md                  # 本说明文件
├── acmart.cls                           # ACM文档类
├── ACM-Reference-Format.bst             # ACM参考文献格式
├── samples/                             # ACM模板示例
└── [其他ACM模板支持文件]
```

---

## 编译方法

### 方法1: 使用批处理脚本 (推荐)
```bash
# 双击或在命令行运行
compile_acm.bat
```

### 方法2: 手动编译
```bash
pdflatex energy_aware_ai_deployment_acm.tex
bibtex energy_aware_ai_deployment_acm
pdflatex energy_aware_ai_deployment_acm.tex
pdflatex energy_aware_ai_deployment_acm.tex
```

### 方法3: 使用LaTeX编辑器
- **Overleaf**: 上传所有文件到项目，选择主文件编译
- **TeXstudio/TeXworks**: 打开主文件，按F5编译
- **VSCode + LaTeX Workshop**: 打开文件夹，编译主文件

---

## 报告特点

### ✅ 符合ACM Sigconf标准
- **页面长度**: ~4页 (满足3-3.5页最小要求)
- **格式规范**: 双栏布局，标准字体和间距
- **参考文献**: ACM标准格式
- **CCS分类**: 包含计算分类系统标签

### 📊 核心内容结构
1. **Introduction**: 研究背景与问题定义
2. **Methodology**: 量化策略、硬件评估、能效指标
3. **Results and Analysis**: 实验结果与分析
4. **Deployment Guidelines**: 实际部署建议
5. **Conclusions**: 总结与展望

### 🔬 技术贡献
- **量化-硬件协同优化框架**
- **EOR和TWEOR能效评估指标**
- **系统性部署指导方案**

---

## 关键数据摘要

| 指标 | 数值 | 说明 |
|------|------|------|
| **能源减少** | 25% | INT8量化最佳效果 |
| **协同优化** | 40% | A100+INT8组合收益 |
| **准确率保持** | 98%+ | 量化后性能维持 |
| **知识蒸馏** | 19.8% | 额外能源节省 |

---

## 课程要求对照

### ✅ 研究项目要求
- [x] **页数**: 3-3.5页最小 (当前~4页)
- [x] **模板**: ACM Sigconf模板
- [x] **团队**: 3人团队 (边昊济、王子楠、吕任远)
- [x] **主题**: 嵌入式AI相关 (能源感知AI部署)

### ✅ 技术规范
- [x] **文档类**: `\documentclass[sigconf,review]{acmart}`
- [x] **参考文献**: ACM-Reference-Format格式
- [x] **CCS概念**: 机器学习、神经网络、能源网络
- [x] **关键词**: 能源效率、模型量化、硬件优化等

---

## 编译问题解决

### 常见错误及解决方案

**1. 字体错误**
```
解决方案: 确保安装了完整的LaTeX发行版 (TeX Live/MiKTeX)
```

**2. 类文件未找到**
```
错误: acmart.cls not found
解决方案: 确保acmart.cls文件在同一目录下
```

**3. 参考文献格式问题**
```
解决方案: 确保ACM-Reference-Format.bst文件存在，运行完整编译流程
```

**4. 中文支持问题**
```
解决方案: 本模板使用英文，如需中文支持需要额外配置
```

---

## 提交清单

提交时请确保包含以下文件：

### 📄 必需文件
- [x] `energy_aware_ai_deployment_acm.pdf` - 最终PDF报告
- [x] `energy_aware_ai_deployment_acm.tex` - LaTeX源文件
- [x] 所有ACM模板支持文件

### 💻 代码文件 (如适用)
- [ ] 实验代码
- [ ] 数据处理脚本
- [ ] 结果分析脚本

### 📊 补充材料 (可选)
- [ ] 详细实验数据
- [ ] 额外可视化图表
- [ ] 演示文稿材料

---

## 版本信息

- **创建日期**: 2025年1月
- **模板版本**: ACM Sigconf 2025
- **LaTeX引擎**: pdfLaTeX
- **字符编码**: UTF-8

---

## 联系信息

如有技术问题或需要修改，请联系：

- **边昊济**: haojibian2027@u.northwestern.edu (量化技术)
- **王子楠**: zinanwang2027@u.northwestern.edu (硬件评估)
- **吕任远**: renyuanlu2027@u.northwestern.edu (能效指标)

---

## 致谢

感谢CE 495 Energy-Aware Intelligence课程提供的研究机会，以及ACM提供的标准化模板格式。

**祝编译顺利！** 🎓 