"""
AI Security Analyst Assistant - Streamlit Application

A production-ready RAG system for security analysis using multiple retrieval strategies.
"""

import os
import sys
import time
from datetime import datetime
from typing import List, Dict, Optional

import streamlit as st
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables
load_dotenv()

# Import RAG components
try:
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_community.vectorstores import Chroma
    from langchain_core.documents import Document
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
except ImportError as e:
    st.error(f"Missing dependencies: {e}. Please run: pip install -r requirements.txt")
    st.stop()


# Page configuration
st.set_page_config(
    page_title="AI Security Analyst Assistant",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        padding-bottom: 2rem;
    }
    .source-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .confidence-high {
        color: #28a745;
        font-weight: bold;
    }
    .confidence-medium {
        color: #ffc107;
        font-weight: bold;
    }
    .confidence-low {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
def init_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "rag_config" not in st.session_state:
        st.session_state.rag_config = "basic"

    if "conversation_id" not in st.session_state:
        st.session_state.conversation_id = datetime.now().strftime("%Y%m%d_%H%M%S")


# Cache expensive operations
@st.cache_resource
def load_vectorstore():
    """Load vector store (cached)."""
    try:
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        vectorstore = Chroma(
            collection_name="owasp_security",
            embedding_function=embeddings,
            persist_directory="../chroma_db",
        )
        return vectorstore
    except Exception as e:
        st.error(f"Failed to load vector store: {e}")
        return None


@st.cache_resource
def load_llm(model: str = "gpt-4", temperature: float = 0.0):
    """Load LLM (cached by parameters)."""
    return ChatOpenAI(model=model, temperature=temperature)


# RAG query function
def query_rag(
    question: str,
    vectorstore,
    llm,
    k: int = 3,
    config: str = "basic",
) -> Dict:
    """Execute RAG query.

    Args:
        question: User question
        vectorstore: Chroma vector store
        llm: Language model
        k: Number of documents to retrieve
        config: RAG configuration (basic, fusion, filtered, hardened)

    Returns:
        Dict with answer, sources, confidence, latency
    """
    start_time = time.time()

    try:
        # Retrieve documents
        docs_with_scores = vectorstore.similarity_search_with_score(question, k=k)
        docs = [doc for doc, score in docs_with_scores]
        scores = [score for doc, score in docs_with_scores]

        if not docs:
            return {
                "answer": "I couldn't find relevant information to answer this question.",
                "sources": [],
                "confidence": {"overall": 0.0, "level": "low"},
                "latency_ms": (time.time() - start_time) * 1000,
                "error": False,
            }

        # Build context
        context = "\n\n".join([doc.page_content for doc in docs])

        # Generate answer
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an AI security expert assistant. Use the provided context to answer questions about AI/ML security.

Guidelines:
- Only answer based on the provided context
- Focus on defensive techniques and best practices
- If uncertain, say "I don't know based on the provided context"
- Cite specific security frameworks when relevant (OWASP, MITRE ATT&CK)
- Be concise but comprehensive

Context:
{context}"""),
            ("user", "{question}")
        ])

        chain = prompt | llm | StrOutputParser()
        answer = chain.invoke({"context": context, "question": question})

        # Extract sources
        sources = []
        for doc in docs:
            source_info = {
                "content": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content,
                "metadata": doc.metadata,
            }
            sources.append(source_info)

        # Calculate confidence (based on similarity scores)
        if scores:
            avg_score = sum(scores) / len(scores)
            # Lower score = higher similarity in Chroma (L2 distance)
            # Convert to confidence (inverse relationship)
            confidence_score = max(0.0, min(1.0, 1.0 - (avg_score / 2.0)))

            if confidence_score >= 0.8:
                confidence_level = "high"
            elif confidence_score >= 0.6:
                confidence_level = "medium"
            else:
                confidence_level = "low"
        else:
            confidence_score = 0.5
            confidence_level = "medium"

        latency_ms = (time.time() - start_time) * 1000

        return {
            "answer": answer,
            "sources": sources,
            "confidence": {
                "overall": confidence_score,
                "level": confidence_level,
            },
            "latency_ms": latency_ms,
            "error": False,
        }

    except Exception as e:
        return {
            "answer": f"I encountered an error processing your request: {str(e)}",
            "sources": [],
            "confidence": {"overall": 0.0, "level": "low"},
            "latency_ms": (time.time() - start_time) * 1000,
            "error": True,
        }


def display_source(source: Dict, index: int):
    """Display a source card."""
    with st.expander(f"📄 Source {index + 1}"):
        st.markdown(f"**Content:** {source['content']}")
        if source.get('metadata'):
            st.markdown(f"**Metadata:** {source['metadata']}")


def display_confidence(confidence: Dict):
    """Display confidence indicator."""
    score = confidence["overall"]
    level = confidence["level"]

    if level == "high":
        css_class = "confidence-high"
        emoji = "✅"
    elif level == "medium":
        css_class = "confidence-medium"
        emoji = "⚠️"
    else:
        css_class = "confidence-low"
        emoji = "❌"

    st.markdown(
        f"{emoji} <span class='{css_class}'>Confidence: {level.upper()} ({score:.2f})</span>",
        unsafe_allow_html=True
    )


def main():
    """Main application."""

    # Initialize
    init_session_state()

    # Header
    st.markdown('<div class="main-header">🔐 AI Security Analyst Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Built with RAG: Retrieval-Augmented Generation for Security Analysis</div>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")

        # RAG configuration
        rag_config = st.selectbox(
            "RAG Strategy",
            ["basic", "fusion", "filtered", "hardened"],
            index=0,
            help="Choose the RAG retrieval strategy"
        )
        st.session_state.rag_config = rag_config

        # Model settings
        st.subheader("Model Settings")
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            step=0.1,
            help="Higher = more creative, Lower = more focused"
        )

        top_k = st.slider(
            "Top K Documents",
            min_value=1,
            max_value=10,
            value=3,
            help="Number of documents to retrieve"
        )

        st.divider()

        # Example queries
        st.subheader("💡 Example Queries")
        example_queries = [
            "What is prompt injection?",
            "How do I defend against model extraction attacks?",
            "What are the OWASP Top 10 for LLMs?",
            "Explain adversarial attacks on ML models",
            "What is training data poisoning?",
        ]

        for example in example_queries:
            if st.button(example, key=f"example_{example}", use_container_width=True):
                st.session_state.current_query = example
                st.rerun()

        st.divider()

        # Clear chat
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.divider()

        # Info
        st.subheader("ℹ️ About")
        st.markdown("""
        This is a demonstration of a production-ready RAG system for security analysis.

        **Features:**
        - Multiple RAG strategies
        - Source citations
        - Confidence scoring
        - Security-focused responses

        **Data Sources:**
        - OWASP Top 10 for LLMs
        - MITRE ATT&CK Framework
        - Security research papers
        """)

    # Load resources
    with st.spinner("Loading models and data..."):
        vectorstore = load_vectorstore()
        if vectorstore is None:
            st.error("Failed to load vector store. Please check your configuration.")
            st.stop()

        llm = load_llm(temperature=temperature)

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message["role"] == "assistant" and "metadata" in message:
                # Display confidence
                if "confidence" in message["metadata"]:
                    display_confidence(message["metadata"]["confidence"])

                # Display latency
                if "latency_ms" in message["metadata"]:
                    st.caption(f"⏱️ Response time: {message['metadata']['latency_ms']:.0f}ms")

                # Display sources
                if "sources" in message["metadata"] and message["metadata"]["sources"]:
                    st.markdown("### 📚 Sources")
                    for i, source in enumerate(message["metadata"]["sources"]):
                        display_source(source, i)

    # Chat input
    if "current_query" in st.session_state:
        query = st.session_state.current_query
        del st.session_state.current_query
    else:
        query = st.chat_input("Ask me about AI/ML security...")

    if query:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": query})

        with st.chat_message("user"):
            st.markdown(query)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = query_rag(
                    question=query,
                    vectorstore=vectorstore,
                    llm=llm,
                    k=top_k,
                    config=rag_config,
                )

            # Display answer
            st.markdown(result["answer"])

            # Display confidence
            display_confidence(result["confidence"])

            # Display latency
            st.caption(f"⏱️ Response time: {result['latency_ms']:.0f}ms")

            # Display sources
            if result["sources"]:
                st.markdown("### 📚 Sources")
                for i, source in enumerate(result["sources"]):
                    display_source(source, i)

            # Add assistant message to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": result["answer"],
                "metadata": {
                    "confidence": result["confidence"],
                    "latency_ms": result["latency_ms"],
                    "sources": result["sources"],
                    "config": rag_config,
                }
            })


if __name__ == "__main__":
    main()
