<div align="center">

# ◈ LIFE OF RESEARCH
### 14-Agent Autonomous AI Research Lab
#### By Pranay Mahendrakar

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![PySide6](https://img.shields.io/badge/GUI-PySide6-green?style=for-the-badge)](https://doc.qt.io/qtforpython/)
[![OpenAI](https://img.shields.io/badge/AI-GPT--4o-orange?style=for-the-badge&logo=openai)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-5.0-purple?style=for-the-badge)](https://github.com/PranayMahendrakar/life-of-research)

**🔬 Generate publication-quality research papers autonomously using a 14-agent AI pipeline with iterative peer review, debate mode, humanization engine, and journal-quality evaluation.**

[🚀 Live Demo](https://PranayMahendrakar.github.io/life-of-research) · [📖 Documentation](#documentation) · [⚡ Quick Start](#quick-start) · [🏆 Features](#features)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **14 Specialized AI Agents** | From Research Director to Journal Evaluator |
| **Iterative Loop System** | Automatically improves papers until target score |
| **Peer Review Panel** | Methods, Novelty, and Harsh reviewers |
| **Debate Mode** | Author rebuttal agent defends against reviewers |
| **Humanization Engine** | Removes AI patterns, adds researcher voice |
| **Live Streaming** | Real-time token-by-token output with markdown rendering |
| **Score Visualization** | Animated score rings, progress graphs |
| **Knowledge Graph** | Visual topic relationship map |
| **Multi-format Export** | DOCX, Markdown, HTML, Plain Text |
| **5 Citation Styles** | IEEE, APA, ACM, Springer, NeurIPS |
| **6 Paper Types** | Research Paper, Survey, Thesis, Proposal, etc. |

---

## 🤖 The 14-Agent Pipeline

```
◈ Research Director  →  📚 Literature Intelligence  →  💡 Hypothesis Generator
                                    ↓
                          ✍ Academic Writer (Loop Start)
                         ↙          ↓          ↘
              ⚗ Methods      🔭 Novelty      ⚡ Harsh
              Reviewer       Reviewer        Reviewer
                         ↘          ↓          ↙
                           🛡 Argument Defender
                                    ↓
                          ⚙ Correction Engine
                                    ↓
                          🧬 Humanization Engine
                                    ↓
                          ★ Journal Evaluator
                                    ↓
                    [Score ≥ Target? → Done : Loop Again]
```

---

## ⚡ Quick Start

### Prerequisites

- Python 3.9 or higher
- OpenAI API Key (GPT-4o recommended)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/PranayMahendrakar/life-of-research.git
cd life-of-research

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python life_of_research_app.py
```

### Dependencies

```
PySide6>=6.5.0       # Qt6 GUI Framework
requests>=2.31.0     # OpenAI API streaming
python-docx>=1.1.0   # Word document export
```

---

## 📖 Documentation

### Configuration Panel

| Setting | Description | Default |
|---------|-------------|---------|
| **API Key** | Your OpenAI API key (sk-...) | Required |
| **Model** | GPT model to use | gpt-4o |
| **Topic** | Research topic/title | Required |
| **Paper Type** | Type of academic paper | Original Research |
| **Citation Style** | Reference format | IEEE |
| **Max Loops** | Maximum iteration cycles | 3 |
| **Stop Score** | Target quality score | 8.0/10 |
| **Debate Mode** | Enable author rebuttal | ON |

### How It Works

1. **Research Direction**: The Director agent analyzes your topic and creates a structured research plan
2. **Literature Review**: The Scholar agent generates realistic literature analysis and citations
3. **Hypothesis Generation**: Scientific reasoner creates testable hypotheses and experiment designs
4. **Writing Loop**: The pipeline iterates through writing → review → defense → correction → humanization
5. **Evaluation**: Journal Evaluator scores the paper (0-10) and checks against your target
6. **Auto-improvement**: If score < target, the loop repeats with reviewer feedback incorporated

### Achievement System

| Achievement | Score Threshold |
|------------|----------------|
| 🌟 GOOD PAPER | 7.0+ |
| 🏆 PUBLISHABLE QUALITY | 8.0+ |
| 🚀 CONFERENCE READY | 8.5+ |
| 💎 OUTSTANDING RESEARCH | 9.0+ |
| 👑 WORLD CLASS PAPER | 9.5+ |

### Export Formats

- **Word Document (.docx)** — Full formatted document with title page, sections, review panel
- **Markdown (.md)** — Complete paper with all sections in GitHub-flavored markdown
- **HTML (.html)** — Styled standalone webpage, ready to share
- **Plain Text (.txt)** — Clean text for further processing

---

## 🎮 Interface Overview

```
┌─────────────────────────────────────────────────────────────┐
│  ◈ LIFE OF RESEARCH  v5.0                    00:00:00       │
├──────────────┬──────────────────────────┬───────────────────┤
│  LEFT PANEL  │    CENTER FEED (LIVE)    │    RIGHT PANEL    │
│              │                          │                   │
│  • API Key   │  Agent conversation      │  ★ Score Rings    │
│  • Model     │  bubbles with:           │  • Score Graph    │
│  • Topic     │   - Rendered Markdown    │  • Threshold Bar  │
│  • Settings  │   - Raw text             │                   │
│              │   - Word count           │  ⚙ Pipeline       │
│  ▶ LAUNCH    │   - Status indicator     │  • Agent status   │
│  ■ ABORT     │                          │  • Progress       │
│  ⬇ EXPORT   │  ══ ITERATION N/M ══     │                   │
│              │                          │  🕸 Knowledge     │
│  [Particles] │  [Glow Progress Bar]     │  Graph            │
│              │                          │                   │
│              │                          │  🧠 Memory        │
│              │                          │  Browser          │
└──────────────┴──────────────────────────┴───────────────────┘
```

---

## 🛠 Tech Stack

- **GUI**: PySide6 (Qt6 for Python)
- **AI**: OpenAI GPT-4o via streaming API
- **Rendering**: Custom Markdown → HTML converter
- **Animations**: QPainter-based particle system, animated score rings
- **Export**: python-docx for Word documents
- **Architecture**: Multi-threaded (QThread per agent)

---

## 📊 Sample Output

After a complete run, you'll receive:

- ✅ Full research paper (2500+ words)
- ✅ Literature analysis with 10-15 references  
- ✅ Three independent peer reviews
- ✅ Author rebuttal and revision
- ✅ Humanized final version
- ✅ Quality score with detailed scorecard
- ✅ Exportable in 4 formats

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Pranay M Mahendrakar**

- 🌐 Website: [https://sonytech.in/pranay](https://sonytech.in/pranay)
- 💼 GitHub: [@PranayMahendrakar](https://github.com/PranayMahendrakar)
- 🆔 ORCID: [0009-0003-7224-029X](https://orcid.org/0009-0003-7224-029X)

---

<div align="center">

**⭐ If you find this project useful, please star it on GitHub! ⭐**

*Life Of Research — Automating the research pipeline, one paper at a time*

</div>
