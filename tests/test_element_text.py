
import unittest
from computer_use_demo.tools.element_text import ElementTextExtractor
from computer_use_demo.tools.dom_interface import DOMElement

class TestElementTextExtractor(unittest.TestCase):
    def setUp(self):
        self.element = DOMElement(
            tag="p",
            attributes={"class": "test"},
            content="Test Content\nWith Newlines"
        )
        self.extractor = ElementTextExtractor(self.element)
        
    def test_get_text(self):
        text = self.extractor.get_text()
        self.assertEqual(text, "Test Content\nWith Newlines")
        
    def test_get_inner_text(self):
        text = self.extractor.get_inner_text()
        self.assertEqual(text, "Test Content\nWith Newlines")
        
    def test_text_with_attributes(self):
        result = self.extractor.text_with_attributes()
        self.assertIn('text', result)
        self.assertIn('attributes', result)
        self.assertEqual(result['attributes'], {"class": "test"})
