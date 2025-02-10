
import unittest
from computer_use_demo.tools.content_extractor import ContentExtractor
from computer_use_demo.tools.dom_interface import DOMElement
from computer_use_demo.tools.content_processor import ContentProcessor

class TestContentExtraction(unittest.TestCase):
    def setUp(self):
        self.element = DOMElement(
            tag="div",
            attributes={},
            content="  Test   Content  with  spaces  "
        )
        self.extractor = ContentExtractor(self.element)
        
    def test_text_extraction(self):
        text = self.extractor.extract_text()
        self.assertEqual(text, "Test Content with spaces")
        
    def test_structured_content(self):
        content = self.extractor.extract_structured_content()
        self.assertIn('text', content)
        self.assertIn('tag', content)
        self.assertIn('attributes', content)

class TestContentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ContentProcessor()
        
    def test_script_removal(self):
        content = "Text<script>alert('test')</script>More text"
        cleaned = self.processor.remove_scripts(content)
        self.assertEqual(cleaned, "TextMore text")
        
    def test_whitespace_cleaning(self):
        content = "  Multiple   Spaces   Here  "
        cleaned = self.processor.clean_whitespace(content)
        self.assertEqual(cleaned, "Multiple Spaces Here")
