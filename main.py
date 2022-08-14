from src.session import Session
from  src.codebuildRun import Codebuild_run 
from src.eventBridgeRule import Eventbridge_rule
from src.ssmSendCommand import Ssm_send_command
from src.autoscalingUpdate import Autoscaling_update
from src.ecsCommands import Ecs_commands
from src.varibales import *


g_aws_computer_profile          = "campus-yotam"
g_mfa_serial                    = None
g_mfa_token                     = None
g_project_name                  = "testing-script-project"
g_secondery_sources_override    = ""
g_event_rule_name               = "Timely-backup-environment-sync"
g_remote_instance_id            = ["i-0356df9e847cc6655"]
g_remote_commands_comment       = turn_to_prod_comment
g_remote_commands_uncomment     = turn_to_prod_uncomment
g_auto_scaling_group_name       = "EC2ContainerService-ECS-test-EcsInstanceAsg-EFJXQZOBIYKT"
g_ecs_cluster                   = "ECS-test"
g_ecs_service                   = "web-test1"


if __name__ == '__main__':

    session = Session(g_aws_computer_profile, g_mfa_serial)
    if g_mfa_serial:
        session.MFALogin(g_mfa_token)

    # codebuildRun = Codebuild_run(session.GetSession(),g_project_name)
    # response = codebuildRun.Runcodebuild()
    # print(response)

    # eventBridgeRule = Eventbridge_rule(session.GetSession(), g_event_rule_name)
    # response = eventBridgeRule.enableRule()
    # print(response)

    # ssmSendCommand = Ssm_send_command(session.GetSession(), g_remote_instance_id)
    # ssmSendCommand.RunCommands(g_remote_commands_comment)
    # ssmSendCommand.RunCommands(g_remote_commands_uncomment)

    # autoscaling_update = Autoscaling_update(session.GetSession(), g_auto_scaling_group_name)
    # autoscaling_update.updateGroupCapacity(4)
    # autoscaling_update.validateUpdate(4)

    ecsClass = Ecs_commands(session.GetSession(),g_ecs_cluster, g_ecs_service)
    ecsClass.setOriginalValues()
    print(f"desired: {ecsClass.__originalDesired} max: {ecsClass.__originalMax} min: {ecsClass.__originalMin}")
    




