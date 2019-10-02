import unittest
from unittest.mock import Mock

from ExceptionManager import ExceptionManager

from Exceptions.ErrorInternetDisconnected import ErrorInternetDisconnected
from Exceptions.ErrorConnectionReset import ErrorConnectionReset

from Exceptions.ErrorCacheMiss import ErrorCacheMiss
from Exceptions.ErrorSSLProtocolError import ErrorSSLProtocolError

from Stubs.Sender import Sender
from Stubs.CriticalVerifier import CriticalVerifier

class TestExceptionManager(unittest.TestCase):

    def setUp(self):
        self.manager = ExceptionManager(Sender())
        self.manager.Verifier = CriticalVerifier()

    def test_is_exception_type_exception(self):
        self.assertTrue(self.manager.isExceptionType(ErrorInternetDisconnected))
        self.assertTrue(self.manager.isExceptionType(ErrorConnectionReset))
        self.assertTrue(self.manager.isExceptionType(MemoryError))
        self.assertTrue(self.manager.isExceptionType(OSError))

    def test_is_exception_type_not_exception(self):
        self.assertFalse(self.manager.isExceptionType(Sender))
        self.assertFalse(self.manager.isExceptionType(CriticalVerifier))

    def test_is_critical_exception_critical(self):
        self.assertTrue(self.manager.isCriticalException(ErrorInternetDisconnected))
        self.assertTrue(self.manager.isCriticalException(ErrorConnectionReset))
        self.assertTrue(self.manager.isCriticalException(MemoryError))
        self.assertTrue(self.manager.isCriticalException(OSError))

    def test_is_critical_exception_not_critical(self):
        self.assertFalse(self.manager.isCriticalException(ErrorSSLProtocolError))
        self.assertFalse(self.manager.isCriticalException(ErrorCacheMiss))
        self.assertFalse(self.manager.isCriticalException(ImportError))

    def test_handle_not_zero(self):
        self.manager.handle(ErrorInternetDisconnected)
        self.manager.handle(ErrorConnectionReset)
        self.manager.handle(ErrorCacheMiss)

        self.assertTrue(self.manager.CriticalExceptionCounter == 2)
        self.assertTrue(self.manager.NotCriticalExceptionCounter == 1)

    def test_sender(self):
        mock = Mock()
        mock.sendExceptionToServer.return_value = False

        self.manager = ExceptionManager(mock)
        self.manager.Verifier = CriticalVerifier()

        self.manager.handle(ErrorInternetDisconnected)
        self.manager.handle(ErrorConnectionReset)

        self.assertTrue(self.manager.ServerSendingErrorCounter == 2)


