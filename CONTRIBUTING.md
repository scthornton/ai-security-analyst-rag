# Contributing to Security RAG From Scratch

Thank you for your interest in contributing to this project! This is primarily an educational and portfolio project, but contributions that improve the learning experience are welcome.

## Ways to Contribute

### 1. Report Issues
- **Bugs**: Found a bug? Open an issue with:
  - Clear description of the problem
  - Steps to reproduce
  - Expected vs actual behavior
  - Your environment (Python version, OS, dependencies)
  
- **Documentation**: Unclear explanations? Typos? Let us know!

- **Enhancements**: Ideas for improving the educational content or adding new techniques.

### 2. Suggest Improvements
- Additional RAG techniques to demonstrate
- Alternative security data sources
- Better evaluation metrics
- Performance optimizations
- Deployment improvements

### 3. Submit Pull Requests

#### Before You Start
1. Open an issue first to discuss major changes
2. Check existing issues and PRs to avoid duplicates
3. Fork the repository
4. Create a feature branch from `main`

#### Development Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/security-rag-from-scratch.git
cd security-rag-from-scratch

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

#### Code Guidelines
- **Notebooks**: Keep educational and self-contained
  - Clear markdown explanations
  - Well-commented code
  - Example outputs included
  - Run from start to finish without errors

- **Python Code**: Follow PEP 8
  - Use type hints where appropriate
  - Add docstrings for functions
  - Keep functions focused and testable

- **Documentation**: 
  - Update README if adding features
  - Document new dependencies in requirements.txt
  - Add comments explaining complex logic

#### Testing
- Test notebooks end-to-end before submitting
- Ensure all code cells execute successfully
- Verify outputs are informative and correct
- Check for API key requirements

#### Commit Messages
Use clear, descriptive commit messages:
```
Add metadata filtering example for CVE queries
Fix tokenization bug in Part 8 ColBERT implementation
Update requirements.txt with missing dependency
Improve documentation for RAPTOR hierarchical retrieval
```

#### Pull Request Process
1. Update documentation as needed
2. Ensure your code follows project conventions
3. Test thoroughly
4. Create PR with:
   - Clear title and description
   - Reference related issues
   - List of changes made
   - Any breaking changes noted

## Content Guidelines

### Educational Focus
This project is designed for learning. Contributions should:
- Be beginner-friendly with clear explanations
- Include practical examples
- Show both successes and trade-offs
- Reference authoritative sources

### Security Considerations
- Use only defensive security techniques
- Cite authoritative security sources (MITRE, OWASP, NIST)
- Avoid demonstrating actual exploits
- Include security best practices

### Code Quality
- Prioritize readability over cleverness
- Use meaningful variable names
- Include comments for complex logic
- Follow existing code style

## Adding New Techniques

If proposing a new RAG technique:
1. Create a new notebook following the existing pattern
2. Include:
   - Overview and motivation
   - Implementation with explanations
   - Security-relevant examples
   - Comparison with existing techniques
   - When to use this approach
3. Update the main README
4. Add to the learning progression

## Questions?

- Open an issue for general questions
- Check existing documentation first
- Be respectful and constructive

## Code of Conduct

Please note that this project follows a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## Attribution

Contributors will be acknowledged in the project. If you make significant contributions, you'll be added to a CONTRIBUTORS file.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make this educational resource better!
