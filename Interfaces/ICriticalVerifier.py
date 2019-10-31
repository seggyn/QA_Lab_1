import zope.interface


class ICriticalVerifier(zope.interface.Interface):

    def isCriticalException(exception):
        """Verify is exception critical"""