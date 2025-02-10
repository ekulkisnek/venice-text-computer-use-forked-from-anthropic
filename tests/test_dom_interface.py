
import unittest
from computer_use_demo.tools.dom_interface import DOMInterface, DOMElement
from computer_use_demo.tools.query_builder import QueryBuilder

class TestDOMInterface(unittest.TestCase):
    def setUp(self):
        self.dom = DOMInterface()
        self.test_element = DOMElement(
            tag="div",
            attributes={"class": "test"},
            content="Test Content"
        )
        
    def test_query_builder(self):
        builder = QueryBuilder()
        query = builder.by_id("test-id").by_class("test-class").build()
        self.assertEqual(query, "#test-id.test-class")
        
        query = builder.by_tag("div").by_attribute("data-test", "value").build()
        self.assertEqual(query, "#test-id.test-classdiv[data-test='value']")

class TestDOMElement(unittest.TestCase):
    def setUp(self):
        self.element = DOMElement(
            tag="div",
            attributes={"class": "test", "id": "test-id"},
            content="Test Content"
        )
        
    def test_element_properties(self):
        self.assertEqual(self.element.tag, "div")
        self.assertEqual(self.element.attributes["class"], "test")
        self.assertEqual(self.element.content, "Test Content")
