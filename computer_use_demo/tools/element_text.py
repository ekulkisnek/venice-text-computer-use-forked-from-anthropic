
from typing import Optional, Dict, Any
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
        
    def get_text_content(self) -> str:
        """Get complete text content."""
        if 'text_content' not in self._cache:
            self._cache['text_content'] = self._extract_text_content()
        return self._cache['text_content']
        
    def text_with_formatting(self) -> str:
        """Get text with formatting preserved."""
        if 'formatted_text' not in self._cache:
            self._cache['formatted_text'] = self._extract_formatted_text()
        return self._cache['formatted_text']
        
    def text_with_attributes(self) -> Dict[str, Any]:
        """Get text with element attributes."""
        return {
            'text': self.get_text(),
            'attributes': self.element.attributes
        }
        
    def structured_text(self) -> Dict[str, Any]:
        """Get fully structured text representation."""
        return {
            'plain_text': self.get_text(),
            'formatted_text': self.text_with_formatting(),
            'attributes': self.element.attributes,
            'tag': self.element.tag
        }
        
    def _extract_plain_text(self) -> str:
        """Extract text without formatting."""
        return self.element.content.strip()
        
    def _extract_inner_text(self) -> str:
        """Extract text with basic formatting."""
        return self.element.content
        
    def _extract_text_content(self) -> str:
        """Extract complete text content."""
        return f"{self.element.tag}: {self.element.content}"
        
    def _extract_formatted_text(self) -> str:
        """Extract text with formatting preserved."""
        return self.element.content
