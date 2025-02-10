
from typing import List, Optional, Union
from dataclasses import dataclass

@dataclass
class DOMElement:
    tag: str
    attributes: dict
    content: str
    
class DOMInterface:
    def __init__(self):
        self._cache = {}
        
    def get_element(self, selector: str) -> Optional[DOMElement]:
        """Get single element by selector."""
        raise NotImplementedError
        
    def get_elements(self, selector: str) -> List[DOMElement]:
        """Get multiple elements by selector."""
        raise NotImplementedError
        
    def query_selector(self, query: str) -> Optional[DOMElement]:
        """Execute CSS query and return first match."""
        raise NotImplementedError
        
    def query_selector_all(self, query: str) -> List[DOMElement]:
        """Execute CSS query and return all matches."""
        raise NotImplementedError
