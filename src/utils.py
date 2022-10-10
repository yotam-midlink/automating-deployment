import requests

class urlChecker():
    def __init__(self, originUrl, redirectUrl):
        self._origin = originUrl
        self._redirect = redirectUrl

    def isItRedirect(self):
        return self._redirect == requests.get(self._origin).url

    def isItGetOrigin(self):
        return self._origin == requests.get(self._origin).url