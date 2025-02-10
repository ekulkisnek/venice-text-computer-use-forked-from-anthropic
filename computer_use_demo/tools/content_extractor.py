
from typing import Dict, Any
from .dom_interface import DOMElement

class ContentExtractor:
    def __init__(self, element: DOMElement):
        self.element = element
        
    def extract_text(self) -> str:
        """Extract plain text content."""
        return self._clean_text(self.element.content)
        
    def extract_formatted_text(self) -> str:
        """Extract text with basic formatting preserved."""
        return self._preserve_formatting(self.element.content)
        
    def extract_structured_content(self) -> Dict[str, Any]:
        """Extract content as structured data."""
        return {
            'text': self.extract_text(),
            'tag': self.element.tag,
            'attributes': self.element.attributes
        }
        
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text."""
        return ' '.join(text.split())
        
    def _preserve_formatting(self, text: str) -> str:
        """Preserve basic text formatting."""
        return text.strip()
