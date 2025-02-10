
import unittest
from computer_use_demo.tools.base import ToolResult

class TestToolResult(unittest.TestCase):
    def test_tool_result_fields(self):
        """Test ToolResult doesn't have screenshot fields"""
        result = ToolResult()
        self.assertTrue(hasattr(result, 'output'))
        self.assertTrue(hasattr(result, 'error'))
        self.assertTrue(hasattr(result, 'system'))
        self.assertFalse(hasattr(result, 'base64_image'))
        self.assertFalse(hasattr(result, 'screenshot'))
        
    def test_combine_method(self):
        """Test ToolResult combine method works without screenshot fields"""
        result1 = ToolResult(output="test1")
        result2 = ToolResult(output="test2")
        combined = result1 + result2
        self.assertEqual(combined.output, "test1test2")
