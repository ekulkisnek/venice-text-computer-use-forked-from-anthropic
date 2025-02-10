
import re
from typing import Dict

class TextFormatter:
    def __init__(self):
        self._format_handlers = {
            'plain': self._to_plain_text,
            'html': self._to_html,
            'markdown': self._to_markdown
        }
        
    def format_text(self, text: str, format_type: str) -> str:
        """Format text according to specified format."""
        if format_type not in self._format_handlers:
            raise ValueError(f"Unknown format type: {format_type}")
        return self._format_handlers[format_type](text)
        
    def _to_plain_text(self, text: str) -> str:
        """Convert to plain text."""
        return re.sub(r'[\s\n]+', ' ', text).strip()
        
    def _to_html(self, text: str) -> str:
        """Convert to HTML."""
        return text.replace('\n', '<br/>')
        
    def _to_markdown(self, text: str) -> str:
        """Convert to Markdown."""
        return text.replace('\n\n', '\n\n> ')
