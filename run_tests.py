
import unittest
import asyncio
from tests.test_dom_interface import TestDOMInterface, TestDOMElement
from tests.test_content_extraction import TestContentExtraction, TestContentProcessor
from tests.test_element_text import TestElementTextExtractor

def run_phase2_tests():
    """Run the Phase 2 text extraction related tests"""
    suite = unittest.TestSuite()
    
    # Add Phase 2 test cases
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDOMInterface))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDOMElement))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestContentExtraction))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestContentProcessor))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestElementTextExtractor))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def run_all_tests():
    """Run all tests including original ones"""
    from tests import TestComputerTool, TestToolResult
    
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestComputerTool))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestToolResult))
    run_phase2_tests()

if __name__ == '__main__':
    # Set up event loop for async tests
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        # Change this to run_all_tests() if you want to run everything
        run_phase2_tests()
    finally:
        loop.close()
