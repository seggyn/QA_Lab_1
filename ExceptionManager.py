class ExceptionManager:

    CritiicalExceptionsArray = ['ErrorConnectionReset', 'ErrorInternetDisconnected', 'MemoryError', 'OSError']

    def __init__(self):
        self.CriticalExceptionCounter = 0
        self.NotCriticalExceptionCounter = 0

    def isCriticalException(self, exception):
        return True if exception.__name__ in self.CritiicalExceptionsArray else False

    def handle(self, exception):
        if self.isCriticalException(exception):
            self.CriticalExceptionCounter += 1
        else:
            self.NotCriticalExceptionCounter += 1
