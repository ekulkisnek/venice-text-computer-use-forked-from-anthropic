
from typing import Optional
from .dom_interface import DOMElement

class ElementTextExtractor:
    def __init__(self, element: DOMElement):
        self.element = element
        self._cache = {}
        
    def get_text(self) -> str:
        """Get element text without formatting."""
        if 'plain_text' not in self._cache:
            self._cache['plain_text'] = self._extract_plain_text()
        return self._cache['plain_text']
        
    def get_inner_text(self) -> str:
        """Get inner text with basic formatting."""
        if 'inner_text' not in self._cache:
            self._cache['inner_text'] = self._extract_inner_text()
        return self._cache['inner_text']
        
    def _extract_plain_text(self) -> str:
        """Extract text without formatting."""
        return self.element.content.strip()
        
    def _extract_inner_text(self) -> str:
        """Extract text with basic formatting."""
        return self.element.content
