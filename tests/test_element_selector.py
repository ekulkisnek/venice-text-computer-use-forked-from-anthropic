
import unittest
from computer_use_demo.tools.element_selector import ElementSelector, ElementStateTracker
from computer_use_demo.tools.dom_interface import DOMElement

class TestElementSelector(unittest.TestCase):
    def setUp(self):
        self.selector = ElementSelector()
        self.test_element = DOMElement(
            tag="div",
            attributes={"id": "test-id", "class": "test-class"},
            content="Test Content"
        )

    def test_id_selection(self):
        element = self.selector.select('id', 'test-id')
        self.assertIsNotNone(element)
        self.assertEqual(element.attributes['id'], 'test-id')

    def test_attribute_access(self):
        value = self.selector.get_attribute(self.test_element, 'class')
        self.assertEqual(value, 'test-class')

    def test_attribute_modification(self):
        self.selector.set_attribute(self.test_element, 'data-test', 'value')
        self.assertEqual(self.test_element.attributes['data-test'], 'value')

class TestElementStateTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ElementStateTracker()
        self.changes = []
        
    def test_state_tracking(self):
        def observer(element_id, old_state, new_state):
            self.changes.append((element_id, old_state, new_state))
            
        self.tracker.add_observer(observer)
        self.tracker.track_element('test-id', {'value': 1})
        self.tracker.update_state('test-id', {'value': 2})
        
        self.assertEqual(len(self.changes), 1)
        self.assertEqual(self.changes[0][2]['value'], 2)
