# test_zigspeed.py
"""
Tests for ZigSpeed module.
"""

import unittest
from zigspeed import ZigSpeed

class TestZigSpeed(unittest.TestCase):
    """Test cases for ZigSpeed class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZigSpeed()
        self.assertIsInstance(instance, ZigSpeed)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZigSpeed()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
