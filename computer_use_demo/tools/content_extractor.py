
from typing import Optional, Dict, Any

class ContentExtractor:
    def __init__(self, element):
        self.element = element
        
    def _clean_text(self, text: str) -> str:
        """Clean extracted text."""
        if not text:
            return ""
        return text.strip()
        
    def extract_text(self) -> str:
        """Extract text content from element."""
        if not self.element:
            return ""
        return self._clean_text(self.element.content or "")
        
    def extract_structured_content(self) -> Dict[str, Any]:
        """Extract structured content including text and metadata."""
        if not self.element:
            return {'text': '', 'tag': '', 'attributes': {}}
        return {
            'text': self.extract_text(),
            'tag': self.element.tag,
            'attributes': self.element.attributes
        }
