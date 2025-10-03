# test_recoilatom.py
"""
Tests for RecoilAtom module.
"""

import unittest
from recoilatom import RecoilAtom

class TestRecoilAtom(unittest.TestCase):
    """Test cases for RecoilAtom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RecoilAtom()
        self.assertIsInstance(instance, RecoilAtom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RecoilAtom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
