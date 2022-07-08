

from urllib import response
import pprint 



class Autoscaling_update():
    def __init__(self, session, autoscalingGroup):
        self._client = session
        self._autoscaling = self._client.client('autoscaling')
        self._autoscalingGroup = autoscalingGroup
        self._stopScaling = False
        self._originalMax = 0
        self._originalMin = 0
        self._originalDesired = 0

    def updateGroupCapacityForBackup(self, desiredCapacity):
        self.checkCapacityForBackup(desiredCapacity)
        if (self._stopScaling == False):
            self.saveOriginals()
            self.updateGroupCapacity(desiredCapacity)

    def checkCapacityForBackup(self, desiredCapacity):
        response = self._autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[self._autoscalingGroup])
        desiredCap = response['AutoScalingGroups'][0]['DesiredCapacity']
        if (desiredCap >= desiredCapacity):
            self._stopScaling = True
            print("autoscaling group has alreadedy {dCap} instances".format(dCap = desiredCap))

    def saveOriginals(self):
        response = self._autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[self._autoscalingGroup])
        self._originalDesired = response['AutoScalingGroups'][0]['DesiredCapacity']
        self._originalMax = response['AutoScalingGroups'][0]['MaxSize']
        self._originalMin = response['AutoScalingGroups'][0]['MinSize']

    def updateGroupCapacity(self, desiredCapacity):
        self._autoscaling.update_auto_scaling_group(AutoScalingGroupName=self._autoscalingGroup,
        MinSize=desiredCapacity,
        DesiredCapacity=desiredCapacity )

    def validateUpdate(self, desiredCapacity):
        response = self._autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[self._autoscalingGroup])
        desiredCap = response['AutoScalingGroups'][0]['DesiredCapacity']
        if(desiredCapacity == desiredCap):
            return True
        else:
            return False
        





