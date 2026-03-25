# Security RAG From Scratch

**Building an AI Security Analyst Assistant using Retrieval-Augmented Generation**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-green.svg)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991.svg)](https://openai.com/)

A comprehensive, educational implementation of RAG techniques applied to AI/ML security, suitable for portfolio demonstration and learning advanced retrieval methods.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Learning Path](#learning-path)
- [What You'll Learn](#what-youll-learn)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Notebooks](#notebooks)
- [Security Data Sources](#security-data-sources)
- [Advanced Techniques](#advanced-techniques)
- [Demo Application](#demo-application)
- [Contributing](#contributing)
- [License](#license)
- [Resources](#resources)

## Overview

This project demonstrates how to build a production-ready RAG system for security applications, progressing from basic concepts to advanced techniques like RAPTOR and ColBERT. Each notebook is self-contained and educational, showing the complete implementation process with real security data sources.

## Key Features

🎯 **11 Comprehensive Notebooks** - From basics to production deployment
🔒 **Security-Focused** - Real-world AI/ML security applications
🚀 **Advanced Techniques** - RAPTOR, ColBERT, RAG-Fusion, and more
📊 **Evaluation Framework** - Quantitative metrics for comparison
🛡️ **Security Hardening** - Adversarial detection, PII redaction, source verification
🌐 **Production Ready** - Streamlit app with Docker deployment
📚 **Educational** - Clear explanations and visualizations throughout

## Learning Path

**New to RAG?** Start here:

1. [RAG From Scratch by LangChain](https://github.com/langchain-ai/rag-from-scratch) - Excellent introduction to core RAG concepts (indexing, retrieval, generation)
2. Return to this repo for security-focused advanced techniques and production deployment

**Already know RAG basics?** Start directly with Notebook 1 to see how RAG applies to security applications with advanced retrieval methods, security hardening, and production-ready architecture.

## What You'll Learn

- ✅ RAG fundamentals with security-focused data (MITRE ATT&CK, OWASP, CVEs)
- ✅ Advanced retrieval techniques (multi-query, RAG-fusion, decomposition)
- ✅ Metadata filtering and query structuring for production systems
- ✅ Intelligent re-ranking by security severity and relevance
- ✅ Hierarchical knowledge organization with RAPTOR
- ✅ Late interaction retrieval with ColBERT
- ✅ Security hardening (adversarial query detection, source verification)
- ✅ Evaluation metrics and benchmarking
- ✅ Deployment as a working web application

## Project Structure

```
security-rag-from-scratch/
├── README.md                          # Project overview and setup
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Contribution guidelines
├── SECURITY.md                        # Security policy
├── CODE_OF_CONDUCT.md                 # Community guidelines
├── requirements.txt                   # Python dependencies
├── Dockerfile                         # Docker configuration
├── docker-compose.yml                 # Docker Compose setup
├── notebooks/                         # Educational Jupyter notebooks (11 parts)
│   ├── part_01_introduction.ipynb
│   ├── part_02_basic_rag.ipynb
│   ├── part_03_advanced_retrieval.ipynb
│   ├── part_04_query_decomposition.ipynb
│   ├── part_05_metadata_filtering.ipynb
│   ├── part_06_reranking.ipynb
│   ├── part_07_raptor.ipynb
│   ├── part_08_colbert.ipynb
│   ├── part_09_security_hardening.ipynb
│   ├── part_10_evaluation.ipynb
│   └── part_11_deployment.ipynb
├── data/                              # Security datasets and knowledge bases
│   ├── owasp_llm_top10/
│   ├── mitre_attack/
│   └── README.md
└── app/                               # Production Streamlit application
    ├── app.py                         # Main application
    ├── utils.py                       # Utility functions
    ├── README.md                      # App documentation
    └── .streamlit/
        └── config.toml                # Streamlit configuration
```

## Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API key
- (Optional) Cohere API key for re-ranking
- (Optional) LangSmith account for tracing

### Installation

1. Clone this repository or navigate to the project directory:
```bash
cd security-rag-from-scratch
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file with your API keys
echo "OPENAI_API_KEY=your-key-here" > .env
echo "COHERE_API_KEY=your-key-here" >> .env
echo "LANGCHAIN_API_KEY=your-key-here" >> .env
echo "LANGCHAIN_TRACING_V2=true" >> .env
```

4. Start with Part 1:
```bash
jupyter notebook notebooks/part_01_introduction.ipynb
```

## Notebooks

Each notebook is self-contained and builds upon previous concepts:

1. **Introduction & Use Case** - Understanding the security analyst assistant use case and architecture overview
2. **Basic RAG** - Implementing fundamental RAG with MITRE ATT&CK and OWASP data
3. **Advanced Retrieval** - Multi-query and RAG-fusion for comprehensive results
4. **Query Decomposition** - Breaking complex security questions into manageable sub-questions
5. **Metadata Filtering** - Structured queries for CVE severity, dates, and affected systems
6. **Intelligent Ranking** - Re-ranking by security priority using Cohere and custom logic
7. **RAPTOR** - Hierarchical security knowledge organization (Tactics → Techniques → Procedures)
8. **ColBERT** - Late interaction retrieval for precise matching of vulnerability patterns
9. **Security Hardening** - Making the RAG system itself secure against adversarial queries
10. **Evaluation & Metrics** - Measuring retrieval quality and generation performance
11. **Deployment** - Building and deploying a working Streamlit application

## Security Data Sources

This project uses authoritative security data sources:

- **MITRE ATT&CK Framework** - Adversary tactics, techniques, and procedures
- **OWASP Top 10 for LLMs** - LLM-specific vulnerabilities and mitigations
- **National Vulnerability Database (NVD)** - CVE records with CVSS scores
- **Security Research Papers** - Academic research on adversarial ML and defenses

## Use Cases Demonstrated

- 🔍 Threat intelligence lookup and analysis
- 🛡️ Vulnerability assessment guidance
- 📊 Security framework navigation (MITRE ATT&CK, OWASP)
- 🚨 Incident response recommendations
- 📝 Security policy question answering
- 🔬 Research paper summarization

## Advanced Techniques

### RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval)
Organizes security knowledge hierarchically, enabling both high-level overviews and detailed specifics.

**Use Case**: Navigate MITRE ATT&CK from tactics down to specific procedures, or OWASP categories to specific vulnerability examples.

### ColBERT (Contextualized Late Interaction over BERT)
Token-level embeddings with late interaction scoring for precise matching.

**Use Case**: Find similar code vulnerability patterns, match exploit signatures, search security logs with complex queries.

## Demo Application

Run the interactive demo:

```bash
cd app
streamlit run app.py
```

Features:
- 💬 Natural language security queries
- 📑 Source citations with confidence scores
- ⚙️ Configurable retrieval methods
- 📊 Visualization of retrieval process
- 🔒 Adversarial query detection

## Contributing

Contributions are welcome! This is an educational project focused on learning RAG techniques for security applications.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

**Quick contribution ideas:**
- Add new security data sources
- Implement additional RAG techniques
- Improve documentation and examples
- Fix bugs or improve performance
- Enhance the evaluation framework

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [RAG from Scratch (Original)](https://github.com/langchain-ai/rag-from-scratch)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [ColBERT Paper](https://arxiv.org/abs/2004.12832)
- [RAPTOR Paper](https://arxiv.org/abs/2401.18059)

## License

MIT License - feel free to use for learning purposes.

## Author

**Scott Thornton** - AI/ML Security Engineer

*Building intelligent systems for security operations*

---

⭐ If you found this project helpful, please consider giving it a star on GitHub!

---

## Contact

**Scott Thornton** — AI Security Researcher

- Website: [perfecxion.ai](https://perfecxion.ai/)
- Email: [scott@perfecxion.ai](mailto:scott@perfecxion.ai)
- LinkedIn: [linkedin.com/in/scthornton](https://www.linkedin.com/in/scthornton)
- ORCID: [0009-0008-0491-0032](https://orcid.org/0009-0008-0491-0032)
- GitHub: [@scthornton](https://github.com/scthornton)

**Security Issues**: Please report via [SECURITY.md](SECURITY.md)
