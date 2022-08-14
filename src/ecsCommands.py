import time

class Ecs_commands():
    def __init__(self, session, clusterName, serviceName):
        self._client = session
        self._ecs = self._client.client('ecs')
        self._application_autoscaling = self._client.client('application-autoscaling')
        self.__originalMax = 0
        self.__originalMin = 0
        self.__originalDesired = 0
        self._clusterName = clusterName
        self._serviceName = serviceName
    
    def __getDesiredNum(self):
        response = self._ecs.describe_services(
            cluster = self._clusterName,
            services=[self._serviceName]
        )
        return response['services'][0]['desiredCount']

    def __getMaxNum(self):
        response = self._application_autoscaling.describe_scalable_targets(
            ServiceNamespace='ecs',
            ResourceIds=[f'service/{self._clusterName}/{self._serviceName}']
            )
        return response['ScalableTargets'][0]['MaxCapacity']

    def __getMinNum(self):
        response = self._application_autoscaling.describe_scalable_targets(
            ServiceNamespace='ecs',
            ResourceIds=[f'service/{self._clusterName}/{self._serviceName}']
            )
        return response['ScalableTargets'][0]['MinCapacity']

 
    def setOriginalValues(self):
        self.__originalDesired = self.__getDesiredNum
        self.__originalMax = self.__getMaxNum
        self.__originalMin = self.__getMinNum
    
    def __setMaxAndMin(self, max, min):
        self._application_autoscaling.register_scalable_target(
            ServiceNamespace='ecs',
            ResourceIds=[f'service/{self._clusterName}/{self._serviceName}'],
            ScalableDimension='ecs:service:DesiredCount',
            MaxCapacity=max,
            MinCapacity=min
        )

    def __setDesired(self, desired):
        self._ecs.update_service(
            cluster = self._clusterName,
            service = self._serviceName,
            desiredCount = desired
        )

    def updateServiceCapacity(self, desired, max, min):
        self.__setMaxAndMin(max=max, min=min)
        self.__setDesired(desired=desired)


    def __checkCapacity(self, desired, max, min):
        for i in range(5):
            if (__capacityChanged(desired, max, min)):
                break
            time.sleep(4)

    def __capacityChanged(self, desired, max, min):
        if (
            desired == self.__getDesiredNum() &
            max == self.__getMaxNum &
            min == self.__getMinNum
            ):
            return True

        

    def killTask(self, serviceName):
        taskId = self.getTaskId(serviceName)

    def getTaskId(self, serviceName):
        response = self._ecs.list_tasks(serviceName=serviceName)
        taskArn = response['taskArns'][0]
        print(taskArn)
