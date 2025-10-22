"""
Utility functions for the Security RAG application.
"""

import os
import logging
from datetime import datetime
from typing import Dict, List, Optional
import streamlit as st


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_api_key(key_name: str) -> Optional[str]:
    """Get API key from environment or Streamlit secrets.

    Args:
        key_name: Name of the API key

    Returns:
        API key value or None
    """
    # Try Streamlit secrets first (production)
    try:
        return st.secrets[key_name]
    except (FileNotFoundError, KeyError):
        # Fall back to environment variables (development)
        return os.getenv(key_name)


def log_query(query: str, result: Dict, user_id: str = "anonymous"):
    """Log query metrics for monitoring.

    Args:
        query: User query
        result: RAG result
        user_id: User identifier
    """
    metrics = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "query": query,
        "latency_ms": result.get("latency_ms", 0),
        "confidence": result.get("confidence", {}).get("overall", 0),
        "error": result.get("error", False),
        "sources_count": len(result.get("sources", [])),
        "config": result.get("config", "unknown"),
    }

    logger.info(f"Query metrics: {metrics}")

    return metrics


def format_source_citation(source: Dict) -> str:
    """Format source for citation.

    Args:
        source: Source dictionary with content and metadata

    Returns:
        Formatted citation string
    """
    metadata = source.get("metadata", {})
    source_url = metadata.get("source", "Unknown")
    category = metadata.get("category", "Unknown")

    return f"[{category}] {source_url}"


def calculate_confidence_color(confidence_level: str) -> str:
    """Get color for confidence level.

    Args:
        confidence_level: high, medium, or low

    Returns:
        Color code
    """
    color_map = {
        "high": "#28a745",    # Green
        "medium": "#ffc107",  # Yellow
        "low": "#dc3545",     # Red
    }
    return color_map.get(confidence_level, "#6c757d")  # Default gray


def sanitize_input(text: str, max_length: int = 1000) -> str:
    """Sanitize user input.

    Args:
        text: Input text
        max_length: Maximum allowed length

    Returns:
        Sanitized text
    """
    # Limit length
    text = text[:max_length]

    # Remove leading/trailing whitespace
    text = text.strip()

    return text


def export_chat_history(messages: List[Dict]) -> str:
    """Export chat history as markdown.

    Args:
        messages: List of chat messages

    Returns:
        Markdown-formatted chat history
    """
    md_lines = [
        "# Chat History",
        f"*Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
        ""
    ]

    for i, message in enumerate(messages, 1):
        role = message["role"].capitalize()
        content = message["content"]

        md_lines.append(f"## {i}. {role}")
        md_lines.append(f"{content}")
        md_lines.append("")

        # Add metadata for assistant messages
        if message["role"] == "assistant" and "metadata" in message:
            metadata = message["metadata"]
            if "confidence" in metadata:
                confidence = metadata["confidence"]
                md_lines.append(f"**Confidence:** {confidence['level']} ({confidence['overall']:.2f})")

            if "latency_ms" in metadata:
                md_lines.append(f"**Response Time:** {metadata['latency_ms']:.0f}ms")

            if "sources" in metadata and metadata["sources"]:
                md_lines.append(f"**Sources:** {len(metadata['sources'])} documents")

            md_lines.append("")

    return "\n".join(md_lines)
