import unittest
import pytest
from logger import Logger

class TestLogger(unittest.TestCase):
    """
    Test cases for the Logger class.
    """
    def test_logger(self):
        """
        Test the logger's output.
        """
        logger = Logger("test_logger")
        logger.success("Test success message")
        logger.info("Test info message")
        logger.warning("Test warning message")
        logger.error("Test error message")
        logger.debug("Test debug message")
        # assert "INFO: Test info message" in captured.out
        # assert "WARNING: Test warning message" in captured.out
        # assert "ERROR: Test error message" in captured.out
        # assert "DEBUG: Test debug message" in captured.out