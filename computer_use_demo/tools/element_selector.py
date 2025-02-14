
from typing import Optional, List, Dict, Any
from .dom_interface import DOMElement

class ElementStateTracker:
    def __init__(self):
        self._states: Dict[str, Dict[str, Any]] = {}
        self._observers = []

    def track_element(self, element_id: str, initial_state: Dict[str, Any]):
        self._states[element_id] = initial_state

    def update_state(self, element_id: str, new_state: Dict[str, Any]):
        if element_id in self._states:
            old_state = self._states[element_id].copy()
            self._states[element_id].update(new_state)
            self._notify_observers(element_id, old_state, new_state)

    def add_observer(self, observer):
        self._observers.append(observer)

    def _notify_observers(self, element_id: str, old_state: Dict[str, Any], new_state: Dict[str, Any]):
        for observer in self._observers:
            observer(element_id, old_state, new_state)

class ElementSelector:
    def __init__(self):
        self._strategies = {
            'id': self._id_selector,
            'class': self._class_selector,
            'xpath': self._xpath_selector,
            'css': self._css_selector
        }
        self._state_tracker = ElementStateTracker()
        
    def select(self, strategy: str, selector: str) -> Optional[DOMElement]:
        """Select element using specified strategy."""
        if strategy not in self._strategies:
            raise ValueError(f"Unknown strategy: {strategy}")
        element = self._strategies[strategy](selector)
        if element:
            self._track_element_state(element)
        return element

    def select_all(self, strategy: str, selector: str) -> List[DOMElement]:
        """Select all matching elements using specified strategy."""
        elements = []
        if strategy == 'class':
            elements = self._class_selector_all(selector)
        elif strategy == 'xpath':
            elements = self._xpath_selector_all(selector)
        return elements

    def _id_selector(self, id_: str) -> Optional[DOMElement]:
        """Select element by ID."""
        try:
            return DOMElement(
                tag="div",  # Placeholder - actual implementation would get real tag
                attributes={"id": id_},
                content=""
            )
        except Exception as e:
            raise ValueError(f"Invalid ID selector: {e}")

    def _class_selector(self, class_name: str) -> Optional[DOMElement]:
        """Select first element with given class."""
        elements = self._class_selector_all(class_name)
        return elements[0] if elements else None

    def _class_selector_all(self, class_name: str) -> List[DOMElement]:
        """Select all elements with given class."""
        # Placeholder implementation
        return []

    def _xpath_selector(self, xpath: str) -> Optional[DOMElement]:
        """Select element using XPath."""
        elements = self._xpath_selector_all(xpath)
        return elements[0] if elements else None

    def _xpath_selector_all(self, xpath: str) -> List[DOMElement]:
        """Select all elements matching XPath."""
        # Placeholder implementation
        return []

    def _css_selector(self, css: str) -> Optional[DOMElement]:
        """Select element using CSS selector."""
        # Placeholder implementation
        return None

    def _track_element_state(self, element: DOMElement):
        """Track element state changes."""
        element_id = element.attributes.get('id', str(id(element)))
        initial_state = {
            'tag': element.tag,
            'attributes': element.attributes.copy(),
            'content': element.content
        }
        self._state_tracker.track_element(element_id, initial_state)

    def get_attribute(self, element: DOMElement, attr: str) -> Any:
        """Get element attribute value."""
        return element.attributes.get(attr)

    def set_attribute(self, element: DOMElement, attr: str, value: Any):
        """Set element attribute value."""
        if not isinstance(attr, str):
            raise ValueError("Attribute name must be a string")
        element.attributes[attr] = value
        self._track_element_state(element)
