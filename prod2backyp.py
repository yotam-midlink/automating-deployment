from src.session import Session
from src.codebuildRun import Codebuild_run 
from src.eventBridgeRule import Eventbridge_rule
from src.ssmSendCommand import Ssm_send_command
from src.autoscalingUpdate import Autoscaling_update
from src.ecsCommands import Ecs_commands
from src.varibales import *
from vars import *
import time

# local vars

backupTasks             = 1
sleeptime               = 5


# initial session

session = Session(g_aws_computer_profile, g_mfa_serial)
if g_mfa_serial:
    session.MFALogin(g_mfa_token)

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
backupEcs.updateServiceCapacity(desired=backupTasks, max=backupTasks, min=backupTasks)
time.sleep(sleeptime)
backupEcs.validateCapacity(desired=backupTasks, max=backupTasks, min=backupTasks)

# run ssm command for switching from backuup to production on wp-config. 
# ssmSendCommand = Ssm_send_command(session.GetSession(), g_test_instance_id)
# ssmSendCommand.RunCommands(g_remote_commands_comment)
# ssmSendCommand.RunCommands(g_remote_commands_uncomment)

# stop container  run totalcache flush caches. 


# check if it redirects to production. 


# run scripts of switching cloudfront


# checkout for traffic change. 








