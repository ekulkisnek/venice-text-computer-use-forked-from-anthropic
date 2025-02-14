
import unittest
import asyncio
from tests.test_dom_interface import TestDOMInterface, TestDOMElement
from tests.test_content_extraction import TestContentExtraction, TestContentProcessor
from tests.test_element_text import TestElementTextExtractor

def run_integration_tests():
    """Run integration tests"""
    from tests.integration.test_dom_integration import TestDOMIntegration
    from tests.integration.test_system_integration import TestSystemIntegration
    
    suite = unittest.TestSuite()
    
    # Add integration test cases
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDOMIntegration))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSystemIntegration))
    
    # Run tests with coverage
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def run_all_tests():
    """Run all tests including integration tests"""
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDOMInterface))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDOMElement))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestContentExtraction))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestContentProcessor))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestElementTextExtractor))
    
    # Add integration tests
    from tests.integration.test_dom_integration import TestDOMIntegration
    from tests.integration.test_system_integration import TestSystemIntegration
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDOMIntegration))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSystemIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_all_tests()

if __name__ == '__main__':
    # Set up event loop for async tests
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        run_all_tests()
    finally:
        loop.close()
