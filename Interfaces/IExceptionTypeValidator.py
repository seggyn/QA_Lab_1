import zope.interface

class IExceptionTypeValidator(zope.interface.Interface):

    def isExceptionType(exception):
        '''Check object is exception type'''