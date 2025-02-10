
from typing import List

class QueryBuilder:
    def __init__(self):
        self._query_parts = []
        
    def by_id(self, id_: str) -> 'QueryBuilder':
        """Build query by ID."""
        self._query_parts.append(f"#{id_}")
        return self
        
    def by_class(self, class_name: str) -> 'QueryBuilder':
        """Build query by class name."""
        self._query_parts.append(f".{class_name}")
        return self
        
    def by_tag(self, tag_name: str) -> 'QueryBuilder':
        """Build query by tag name."""
        self._query_parts.append(tag_name)
        return self
        
    def by_attribute(self, attr: str, value: str) -> 'QueryBuilder':
        """Build query by attribute."""
        self._query_parts.append(f"[{attr}='{value}']")
        return self
        
    def build(self) -> str:
        """Combine all parts into final query."""
        return "".join(self._query_parts)
