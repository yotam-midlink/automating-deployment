#  orchestration deployment variables

g_aws_computer_profile          = "campus-yotam"
g_mfa_serial                    = None
g_mfa_token                     = None

# codebuild vars

g_event_rule_name               = "Timely-backup-environment-sync"
g_codebuild_buildspec_verride   = 'arn:aws:s3:::campus-production-deployment/buildspec/buildspec.yml'
g_project_name                  = "sync-production-backup-environment"

# ecs vars

g_ecs_test_cluster              = "ECS-test"
g_ecs_dev_service               = "web-test1"
g_ecs_prod_cluster              = "Campus-Production-Ecs"
g_ecs_prod_service              = "wp-prod"
g_ecs_backup_service            = "wp-backup-prod"

# ssm vars 

g_test_instance_id            = ["i-0356df9e847cc6655"]

