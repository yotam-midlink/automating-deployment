


class Eventbridge_rule():
    def __init__(self, session, eventName):
        self._client = session
        self._eventbridge = self._client.client('events')
        self._eventName = eventName

    def disableRule(self):
        response = self._eventbridge.disable_rule(Name=self._eventName)
        return(response)

    def enableRule(self):
        response = self._eventbridge.enable_rule(Name=self._eventName)
        return(response)
        