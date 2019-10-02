from Stubs.ExceptionTypeValidatorFactory import ExceptionTypeValidatorFactory
import configparser


class ExceptionManager:

    ServerSendingErrorCounter = 0
    CriticalExceptionCounter = 0
    NotCriticalExceptionCounter = 0
    Verifier = None

    def __init__(self, sender):
        self.Sender = sender
        self.Validator = ExceptionTypeValidatorFactory.create()
        self.CriticalExceptionsArray = self.getExceptionsFromConfig()

    def getExceptionsFromConfig(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        string = config['EXCEPTIONS']['critical']
        return string.replace(' ', '').split(',')

    def isExceptionType(self, exception):
        return self.Validator.isExceptionType(exception)

    def isCriticalException(self, exception):
        return self.Verifier.isCriticalException(exception, self.CriticalExceptionsArray)

    def sendExceptionToServer(self, exception):
        self.Sender.sendExceptionToServer(exception)

    def handle(self, exception):
        if self.isExceptionType(exception):
            if self.isCriticalException(exception):
                self.CriticalExceptionCounter += 1
                if not self.sendExceptionToServer(exception):
                    self.ServerSendingErrorCounter += 1
            else:
                self.NotCriticalExceptionCounter += 1
