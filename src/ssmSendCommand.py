import time
from urllib import response

class Ssm_send_command():
    def __init__(self, session, instancesIds):
        self._client = session
        self._ssm = self._client.client('ssm')
        self._instancesIds = instancesIds
        

    def RunCommands(self, commands):
        response = self.SendCommands(commands)
        status = self.GetStatus(response)
        print(status)
    
    def SendCommands(self, commands):
        return self._ssm.send_command(InstanceIds=self._instancesIds, DocumentName="AWS-RunShellScript",Parameters={'commands':[commands]},)

    def GetStatus(self, response):
        command_id = response['Command']['CommandId']
        output = self._ssm.get_command_invocation(CommandId=command_id, InstanceId=self._instancesIds[0])
        while output['Status'] == 'InProgress':
            output = self._ssm.get_command_invocation(CommandId=command_id, InstanceId=self._instancesIds[0])
            print(output)
            time.sleep(3)
        return output
