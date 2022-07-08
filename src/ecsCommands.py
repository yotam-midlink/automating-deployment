

class Ecs_commands():
    def __init__(self, session, prodServiceName, backupServiceName):
        self._client = session
        self._ecs = self._client.client('ecs')
        self._originalMax = 0
        self._originalMin = 0
        self._originalDesired = 0
        self._prodServiceName = prodServiceName
        self._backupServiceName = backupServiceName

    def updateServiceCapacity(self, desired, max, min):
        pass

    def checkCapacity(self, desired, max, min):
        pass

    def killTask(self, serviceName):
        taskId = self.getTaskId(serviceName)

    def getTaskId(self, serviceName):
        response = self._ecs.list_tasks(serviceName=serviceName)
        taskArn = response['taskArns'][0]
        print(taskArn)
