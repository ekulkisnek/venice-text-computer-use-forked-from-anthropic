
import unittest
from computer_use_demo.tools.computer import ComputerTool, Action

class TestComputerTool(unittest.TestCase):
    def setUp(self):
        self.tool = ComputerTool()

    def test_initialization(self):
        """Test ComputerTool initializes without screenshot components"""
        self.assertFalse(hasattr(self.tool, '_screenshot_delay'))
        self.assertFalse(hasattr(self.tool, 'take_screenshot'))
        
    def test_action_types(self):
        """Test available actions don't include screenshot"""
        valid_actions = Action.__args__
        self.assertNotIn('screenshot', valid_actions)
        expected_actions = {
            'key', 'type', 'mouse_move', 'left_click', 
            'left_click_drag', 'right_click', 'middle_click', 
            'double_click', 'cursor_position'
        }
        self.assertEqual(set(valid_actions), expected_actions)

    async def test_mouse_actions(self):
        """Test mouse actions work properly"""
        result = await self.tool(action='mouse_move', coordinate=(100, 100))
        self.assertIsNotNone(result)
        
        result = await self.tool(action='left_click')
        self.assertIsNotNone(result)
