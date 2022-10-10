from src.session import Session
from src.codebuildRun import Codebuild_run 
from src.eventBridgeRule import Eventbridge_rule
from src.ssmSendCommand import Ssm_send_command
from src.autoscalingUpdate import Autoscaling_update
from src.ecsCommands import Ecs_commands
from src.cloudfrontCommands import CloudFront_commands
from src.varibales import *
from src.utils import *
from vars import *
import time

# local vars

backupTasks                 = 25
backupTestTasks             = 1
sleeptime                   = 5
timeToRaiseMultipleTasks    = 20
asgDesiredCapacity          = 9

# functions defenitions

def checkIfUrlIsRedirectFromBackupToProd():
    backupUrlChecker = urlChecker(originUrl=g_backup_url, redirectUrl=g_prod_url)
    for i in range(4):
        if(backupUrlChecker.isItRedirect()):
            print("redirected to prod")
            return True
        else:
            backupEcs.resetService()
            backupCloudfront.clearCache()
    print("does not redirect to prod")
    exit(-1)

# initial session

session = Session(g_aws_computer_profile, g_mfa_serial)
if g_mfa_serial:
    session.MFALogin(g_mfa_token)

# initiate cloudfront

backupCloudfront = CloudFront_commands(session.GetSession(), g_cloudfront_backup_distribution)

# running codebuild and stop trigger.

print("running codebuild and stop trigger.")
eventBridgeRule = Eventbridge_rule(session.GetSession(), g_event_rule_name)
eventBridgeRule.disableRule()
if(eventBridgeRule.isDisabled()):
    print("trigger is disabled")
else:
    print("trigger was not disabled stopping script")
    exit(1)

codebuildRun = Codebuild_run(session.GetSession(),g_project_name, g_codebuild_buildspec_verride)
response = codebuildRun.Runcodebuild()
print(response)

time.sleep(sleeptime)

# raising backup scaling group + scaling up ecs backup containers

print("raising backup scaling group + scaling up ecs backup containers")
backupEcs = Ecs_commands(session.GetSession(),g_ecs_prod_cluster, g_ecs_backup_service)
backupEcs.setOriginalValues()
backupEcs.changeTaskDefenition(g_ecs_backup_taskdefenition_pointing_to_prod)
backupEcs.updateServiceCapacity(desired=backupTestTasks, max=backupTestTasks, min=backupTestTasks)
time.sleep(sleeptime)
backupEcs.validateCapacity(desired=backupTestTasks, max=backupTestTasks, min=backupTestTasks)
backupEcs.validateTaskDefnition(g_ecs_backup_taskdefenition_pointing_to_prod)
backupCloudfront.clearCache()

checkIfUrlIsRedirectFromBackupToProd()

# raising up instances and tasks

productionAsg = Autoscaling_update(session.GetSession(), g_auto_scaling_group_prod)
productionAsg.updateGroupCapacity(asgDesiredCapacity)
time.sleep(sleeptime)
productionAsg.validateUpdate(asgDesiredCapacity)

backupEcs.updateServiceCapacity(backupTasks,backupTasks,backupTasks)
time.sleep(timeToRaiseMultipleTasks)
backupEcs.validateCapacity(backupTasks,backupTasks,backupTasks)

# stop container  run totalcache flush caches. 


# check if it redirects to production. 


# run scripts of switching cloudfront


# checkout for traffic change. 






