import unittest

from ExceptionManager import ExceptionManager

from Exceptions.ErrorInternetDisconnected import ErrorInternetDisconnected
from Exceptions.ErrorConnectionReset import ErrorConnectionReset

from Exceptions.ErrorCacheMiss import ErrorCacheMiss
from Exceptions.ErrorSSLProtocolError import ErrorSSLProtocolError


class TestExceptionManager(unittest.TestCase):

    def setUp(self):
        self.manager = ExceptionManager()

    def test_is_critical_exception_critical(self):
        self.assertTrue(self.manager.isCriticalException(ErrorInternetDisconnected))
        self.assertTrue(self.manager.isCriticalException(ErrorConnectionReset))
        self.assertTrue(self.manager.isCriticalException(MemoryError))
        self.assertTrue(self.manager.isCriticalException(OSError))

    def test_is_critical_exception_not_critical(self):
        self.assertFalse(self.manager.isCriticalException(ErrorSSLProtocolError))
        self.assertFalse(self.manager.isCriticalException(ErrorCacheMiss))
        self.assertFalse(self.manager.isCriticalException(ImportError))

    def test_handle_zero(self):
        self.assertTrue(self.manager.CriticalExceptionCounter == 0)
        self.assertTrue(self.manager.NotCriticalExceptionCounter == 0)

    def test_handle_no_zero(self):
        self.manager.handle(ErrorInternetDisconnected)
        self.manager.handle(ErrorConnectionReset)
        self.manager.handle(ErrorCacheMiss)

        self.assertTrue(self.manager.CriticalExceptionCounter == 2)
        self.assertTrue(self.manager.NotCriticalExceptionCounter == 1)

