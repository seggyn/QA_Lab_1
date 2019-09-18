class CriticalException(Exception):
    def __init__(self, message):
        super().__init__('You have critical exception with description: ' + message)