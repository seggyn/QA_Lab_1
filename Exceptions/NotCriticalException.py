class NotCriticalException(Exception):
    def __init__(self, message):
        super().__init__('You have not critical exception with description: ' + message)