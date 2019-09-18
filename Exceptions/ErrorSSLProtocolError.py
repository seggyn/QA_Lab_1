from Exceptions.NotCriticalException import NotCriticalException


class ErrorSSLProtocolError(NotCriticalException):
    def __init__(self):
        super().__init__('SSL protocol error')
