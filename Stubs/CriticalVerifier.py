import configparser
from zope.interface import implementer
from Interfaces.ICriticalVerifier import ICriticalVerifier


@implementer(ICriticalVerifier)
class CriticalVerifier:

    def isCriticalException(self, exception, array):
        return True if exception.__name__ in array else False