


from operator import truediv


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

    def __getRuleState(self):
        response = self._eventbridge.describe_rule(Name=self._eventName)
        return response['State']

    def isEnabled(self):
        if('ENABLED' == self.__getRuleState()):
            return True
        else:
            return False
    
    def isDisabled(self):
        if('DISABLED' == self.__getRuleState()):
            return True
        else:
            return False
        
        