import zope.interface


class ISender(zope.interface.Interface):

    ServerSendingErrorCounter = zope.interface.Attribute("""Counter of sending to server error""")

    def sendExceptionToServer(exception):
        '''Send exception name to server'''
