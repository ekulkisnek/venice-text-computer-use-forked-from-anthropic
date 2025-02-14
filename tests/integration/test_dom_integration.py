
import unittest
from computer_use_demo.tools.dom_interface import DOMInterface, DOMElement
from computer_use_demo.tools.element_selector import ElementSelector
from computer_use_demo.tools.content_extractor import ContentExtractor
import time
import psutil
import os

class TestDOMIntegration(unittest.TestCase):
    def setUp(self):
        self.dom = DOMInterface()
        self.selector = ElementSelector()
        
    def test_dom_element_selection_integration(self):
        # Create test element and add to DOM
        element = DOMElement(
            tag="div",
            attributes={"id": "test-id", "class": "test-class"},
            content="Test Content"
        )
        self.dom.add_element(element)
        
        # Test element selection
        selected = self.selector.select('id', 'test-id')
        self.assertIsNotNone(selected)
        
        # Test content extraction
        extractor = ContentExtractor(selected)
        content = extractor.extract_text()
        self.assertEqual(content.strip(), "Test Content")

    def test_performance(self):
        start_time = time.time()
        start_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024  # MB
        
        # Perform operations
        for _ in range(1000):
            element = DOMElement(
                tag="div",
                attributes={"id": f"test-{_}", "class": "test"},
                content="Test Content"
            )
            selected = self.selector.select('id', f'test-{_}')
            extractor = ContentExtractor(selected)
            content = extractor.extract_text()
            
        end_time = time.time()
        end_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024  # MB
        
        # Performance assertions
        self.assertLess(end_time - start_time, 2.0)  # Should complete within 2 seconds
        self.assertLess(end_memory - start_memory, 50)  # Should use less than 50MB additional memory
