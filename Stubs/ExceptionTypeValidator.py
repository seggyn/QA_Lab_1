from zope.interface import implementer
from Interfaces.IExceptionTypeValidator import IExceptionTypeValidator


@implementer(IExceptionTypeValidator)
class ExceptionTypeValidator:

    def isExceptionType(self, exception):
        array = ['Exception', 'CriticalException', 'NotCriticalException']
        return True if exception.__bases__[0].__name__ in array else False