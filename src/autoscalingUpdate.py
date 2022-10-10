

from urllib import response
import pprint 
import time

# local variables

sleeptime = 5
countdown = 20



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
            print("Ec2 is not scaling out.")
        else:
            print("autoscaling group has {dCap} instances".format(dCap = desiredCap))
            print("Ec2 is scaling out to {desired}".format(desired = desiredCapacity))

    def saveOriginals(self):
        response = self._autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[self._autoscalingGroup])
        self._originalDesired = response['AutoScalingGroups'][0]['DesiredCapacity']
        self._originalMax = response['AutoScalingGroups'][0]['MaxSize']
        self._originalMin = response['AutoScalingGroups'][0]['MinSize']

    def updateGroupCapacity(self, desiredCapacity):
        self._autoscaling.update_auto_scaling_group(AutoScalingGroupName=self._autoscalingGroup,
        DesiredCapacity=desiredCapacity )
        

    def validateUpdate(self, desiredCapacity):
        time.sleep(sleeptime)
        if(self.validateDesiredCapacity(desiredCapacity) == False):
            print("Desired capacity was not updated.")
            return False

        return self.loopUntilUpdateIsFinish(desiredCapacity) 


    def loopUntilUpdateIsFinish(self, desiredCapacity):
        for i in range(countdown):
            if(self.checkInstanceStatus(desiredCapacity)):
                return True
            time.sleep(sleeptime)
        print("not all instances are updated")
        return False
    
    def checkInstanceStatus(self, desiredCapacity):
        for i in range(desiredCapacity):
            print(i)
            response = self._autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[self._autoscalingGroup])
            instanceStatus = response['AutoScalingGroups'][0]['Instances'][i]['LifecycleState']
            instanceId = response['AutoScalingGroups'][0]['Instances'][i]['InstanceId']
            print(f"instance {instanceId} is {instanceStatus}")
            if(instanceStatus != 'InService'):
                return False
        print(f"{desiredCapacity} instances in service")
        return True

    def validateDesiredCapacity(self, desiredCapacity):
        time.sleep(1)
        response = self._autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[self._autoscalingGroup])
        return response['AutoScalingGroups'][0]['DesiredCapacity'] == desiredCapacity


    def backToOriginals(self):
        self._autoscaling.update_auto_scaling_group(AutoScalingGroupName=self._autoscalingGroup,
        MinSize=self._originalMin,
        DesiredCapacity=self._originalDesired,
        MaxSize=self._originalMax )

        





