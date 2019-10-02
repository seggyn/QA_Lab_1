import zope.interface

class ICriticalVerifier(zope.interface.Interface):

    def isCriticalException():
        """Verify is exception critical"""