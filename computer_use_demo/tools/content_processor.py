
import re
from typing import Optional

class ContentProcessor:
    def remove_scripts(self, content: str) -> str:
        """Remove script tags and contents."""
        return re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
        
    def clean_whitespace(self, content: str) -> str:
        """Clean and normalize whitespace."""
        return ' '.join(content.split())
        
    def normalize_text(self, content: str) -> str:
        """Normalize text content."""
        content = self.remove_scripts(content)
        content = self.clean_whitespace(content)
        return content.strip()
        
    def handle_special_elements(self, content: str) -> str:
        """Handle special HTML elements."""
        # Replace common entities
        replacements = {
            '&nbsp;': ' ',
            '&amp;': '&',
            '&lt;': '<',
            '&gt;': '>'
        }
        for old, new in replacements.items():
            content = content.replace(old, new)
        return content
