from Exceptions.CriticalException import CriticalException


class ErrorConnectionReset(CriticalException):
    def __init__(self):
        super().__init__('Connection reset')