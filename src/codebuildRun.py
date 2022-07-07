from urllib import response
import boto3
import json
import time
from botocore.exceptions import ClientError

class Codebuild_run():
    def __init__(self, session, projectName, secondarySourcesOverride=[]):
        self._client = session
        self._codebuild = self._client.client('codebuild')
        self._projectName = projectName
        self._secondarySourcesOverride = secondarySourcesOverride

    def Runcodebuild(self):
        response = self.StartBuild()
        status = self.GetStatus(response)
        print(status)

    def StartBuild(self):
        response = self._codebuild.start_build(projectName=self._projectName, secondarySourcesOverride=self._secondarySourcesOverride)
        return(response)

    def GetStatus(self, response):
        buildId = self.GetBuildId(response)
        status = self.CheckStatus(buildId)
        return status

    def GetBuildId(self, response):
        return response['build']['id']

    def CheckStatus(self, buildId):
        phase = ""
        while 'COMPLETED'!= phase:
            response = self._codebuild.batch_get_builds(ids=[buildId])
            phase = response['builds'][0]['currentPhase']
            time.sleep(3)
            print(phase)
        status = self._codebuild.batch_get_builds(ids=[buildId])['builds'][0]['buildStatus']
        return status

        
        

    
