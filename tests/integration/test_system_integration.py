
import unittest
from computer_use_demo.tools.dom_interface import DOMInterface, DOMElement
from computer_use_demo.tools.element_selector import ElementSelector
from computer_use_demo.tools.content_extractor import ContentExtractor
from computer_use_demo.tools.element_text import ElementTextExtractor

class TestSystemIntegration(unittest.TestCase):
    def setUp(self):
        self.dom = DOMInterface()
        self.selector = ElementSelector(self.dom)
        self.test_element = DOMElement(
            tag="div",
            attributes={"id": "test-id"},
            content="Test Content"
        )
        self.dom.add_element(self.test_element)
        
    def test_full_system_flow(self):
        # Test complete flow from selection to text extraction
        element = self.selector.select('id', 'test-id')
        content_extractor = ContentExtractor(element)
        text_extractor = ElementTextExtractor(element)
        
        # Test content extraction
        structured_content = content_extractor.extract_structured_content()
        self.assertIn('text', structured_content)
        self.assertIn('tag', structured_content)
        
        # Test text extraction
        text = text_extractor.get_text()
        self.assertIsInstance(text, str)
        
    def test_error_propagation(self):
        # Test invalid selector
        with self.assertRaises(ValueError):
            self.selector.select('invalid_strategy', 'test')
            
        # Test invalid attribute access
        element = self.selector.select('id', 'test-id')
        with self.assertRaises(KeyError):
            _ = element.attributes['nonexistent']
