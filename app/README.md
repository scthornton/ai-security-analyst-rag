# AI Security Analyst Assistant - Streamlit Application

A production-ready web application for the Security RAG system.

## Quick Start

### Local Development

```bash
# 1. Navigate to project root
cd /path/to/security-rag-from-scratch

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Edit .env and add your API keys

# 4. Run the Streamlit app
streamlit run app/app.py

# 5. Open your browser to http://localhost:8501
```

### Docker Deployment

```bash
# 1. Build and run with Docker Compose
docker-compose up --build

# 2. Access the app at http://localhost:8501
```

## Features

- **Interactive Query Interface**: Ask questions about AI/ML security
- **Multiple RAG Strategies**: Choose from basic, fusion, filtered, or hardened RAG
- **Source Citations**: See which documents informed each answer
- **Confidence Scoring**: Understand how reliable each response is
- **Chat History**: Maintain conversation context
- **Example Queries**: Quick start with pre-written security questions

## Configuration

### Environment Variables

See `.env.example` for all available configuration options.

Key variables:
- `OPENAI_API_KEY`: Required for LLM and embeddings
- `LANGCHAIN_API_KEY`: Optional for tracing with LangSmith
- `DEFAULT_MODEL`: LLM model to use (default: gpt-4)
- `DEFAULT_TOP_K`: Number of documents to retrieve (default: 3)

### Streamlit Configuration

Configuration is in `app/.streamlit/config.toml`:
- Theme colors
- Server settings
- Browser options

## Usage

### Example Queries

Try these security questions:
- "What is prompt injection and how do I defend against it?"
- "Explain model extraction attacks"
- "What are the OWASP Top 10 for LLMs?"
- "How do adversarial attacks work on ML models?"

### RAG Strategies

1. **Basic**: Simple retrieval + generation
2. **Fusion**: RAG-Fusion with reciprocal rank fusion
3. **Filtered**: Metadata-based filtering
4. **Hardened**: Security-focused with adversarial detection

## Deployment Options

### Streamlit Cloud

1. Push code to GitHub
2. Visit https://share.streamlit.io/
3. Connect your repository
4. Add secrets (API keys)
5. Deploy!

### AWS/GCP/Azure

See `notebooks/part_11_deployment.ipynb` for detailed deployment guides.

## Troubleshooting

### Common Issues

**Vector store not found:**
```bash
# Make sure you've created the vector store in Part 2
cd notebooks
jupyter notebook part_02_basic_rag.ipynb
# Run the notebook to create chroma_db/
```

**Missing API keys:**
```bash
# Check your .env file
cat .env
# Ensure OPENAI_API_KEY is set
```

**Import errors:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

## Development

### Project Structure

```
app/
├── app.py              # Main Streamlit application
├── utils.py            # Utility functions
├── .streamlit/         # Streamlit configuration
│   └── config.toml
└── README.md           # This file
```

### Adding New Features

1. Edit `app.py` for UI changes
2. Add utility functions to `utils.py`
3. Update configuration in `.streamlit/config.toml`
4. Test locally before deploying

## Support

For issues or questions:
- Check `notebooks/part_11_deployment.ipynb` for detailed documentation
- Review the main project README
- Open an issue on GitHub

## License

See project root LICENSE file.
