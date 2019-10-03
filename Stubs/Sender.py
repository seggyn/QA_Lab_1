from zope.interface import implementer

from Interfaces.ISender import ISender


@implementer(ISender)
class Sender:

    ServerSendingErrorCounter = 0

    def sendExceptionToServer(self, exception):
        '''send exception to server and increase our counter if sending is success'''
        pass
