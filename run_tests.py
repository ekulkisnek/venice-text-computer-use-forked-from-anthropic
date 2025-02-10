
import unittest
import asyncio
from tests import TestComputerTool, TestToolResult

def run_tests():
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestComputerTool))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestToolResult))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
