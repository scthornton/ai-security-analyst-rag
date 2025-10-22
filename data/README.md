# Security Data Directory

This directory contains security datasets and knowledge bases used throughout the notebooks.

## Directory Structure

```
data/
├── README.md                    # This file
├── mitre_attack/               # MITRE ATT&CK Framework data
├── owasp_llm_top10/            # OWASP Top 10 for LLMs content
├── cve_samples/                # Sample CVE records from NVD
└── security_papers/            # Security research papers (optional)
```

## Data Sources

### MITRE ATT&CK Framework
- **Source**: https://attack.mitre.org/
- **Format**: JSON (STIX 2.0)
- **Download**:
  - Visit https://github.com/mitre/cti
  - Or use the MITRE ATT&CK API
- **Contents**: Tactics, Techniques, Sub-techniques, Groups, Software, Mitigations

### OWASP Top 10 for LLMs
- **Source**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **Format**: Markdown/HTML
- **Download**:
  - Clone the OWASP repository
  - Or scrape from the website
- **Contents**: Top 10 LLM vulnerabilities with descriptions, examples, and mitigations

### CVE Samples (National Vulnerability Database)
- **Source**: https://nvd.nist.gov/
- **API**: https://services.nvd.nist.gov/rest/json/cves/2.0
- **Format**: JSON
- **Download**: Use the NVD API (requires API key for higher rate limits)
- **Contents**: CVE records with CVSS scores, descriptions, affected products, references

### Security Research Papers (Optional)
- **Sources**:
  - arXiv (https://arxiv.org/list/cs.CR/recent) - Cryptography and Security
  - arXiv (https://arxiv.org/list/cs.LG/recent) - Machine Learning
  - Conference proceedings (USENIX Security, IEEE S&P, ACM CCS)
- **Format**: PDF or text
- **Topics**: Adversarial ML, model extraction, privacy attacks, defenses, LLM security

## Data Acquisition

The notebooks will include code to download and process these datasets automatically. However, you can also download them manually:

### Quick Start - Download MITRE ATT&CK

```bash
# Create directory
mkdir -p mitre_attack

# Download the Enterprise ATT&CK matrix
curl -o mitre_attack/enterprise-attack.json \
  https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json
```

### Quick Start - OWASP Top 10 for LLMs

The notebooks will scrape this content directly from the OWASP website.

### Quick Start - Sample CVEs

The notebooks will use the NVD API to fetch recent CVEs. You can get an API key at:
https://nvd.nist.gov/developers/request-an-api-key

## Data Processing

Each notebook will include sections for:
1. **Loading** - Reading raw data from files or APIs
2. **Parsing** - Extracting relevant fields and structuring data
3. **Chunking** - Splitting into appropriate sized chunks for embeddings
4. **Enriching** - Adding metadata (severity, dates, categories)
5. **Indexing** - Creating embeddings and storing in vector database

## Privacy and Compliance

All data sources used are:
- ✅ Publicly available
- ✅ Authoritative and maintained
- ✅ Free to use for educational/research purposes
- ✅ Do not contain PII or sensitive information

## Notes

- Large datasets (full NVD database) are excluded from git via .gitignore
- Notebooks will cache processed data to avoid repeated downloads
- Vector store indexes (.chroma, .ragatouille) are also gitignored
- Always verify data source authenticity and integrity
