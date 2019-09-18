from Exceptions.CriticalException import CriticalException


class ErrorInternetDisconnected(CriticalException):
    def __init__(self):
        super().__init__('Internet disconected')
