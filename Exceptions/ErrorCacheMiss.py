from Exceptions.NotCriticalException import NotCriticalException


class ErrorCacheMiss(NotCriticalException):
    def __init__(self):
        super().__init__('Cache miss')
