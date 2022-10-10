#  orchestration deployment variables

g_aws_computer_profile          = "campus-yotam"
g_mfa_serial                    = None
g_mfa_token                     = None
g_backup_url                    = 'https://backup.campus.gov.il/'
g_prod_url                      = 'https://campus.gov.il/'

# codebuild vars

g_event_rule_name               = "Timely-backup-environment-sync"
g_codebuild_buildspec_verride   = 'arn:aws:s3:::campus-production-deployment/buildspec/buildspec.yml'
g_project_name                  = "sync-production-backup-environment"

# asg vars

g_auto_scaling_group_prod       = "EC2ContainerService-Campus-Production-Ecs-EcsInstanceAsg-19SMYS4NHDACR"

# ecs vars

g_ecs_test_cluster              = "ECS-test"
g_ecs_dev_service               = "web-test1"
g_ecs_prod_cluster              = "Campus-Production-Ecs"
g_ecs_prod_service              = "wp-prod"
g_ecs_backup_service            = "wp-backup-prod"
g_ecs_backup_taskdefenition_pointing_to_backup = "arn:aws:ecs:eu-west-1:749395632050:task-definition/wp-backaup-production:7"
g_ecs_backup_taskdefenition_pointing_to_prod   = "arn:aws:ecs:eu-west-1:749395632050:task-definition/wp-backaup-production:5"

# ssm vars 

g_test_instance_id            = ["i-0356df9e847cc6655"]

# cloudfront

g_cloudfront_backup_distribution = "E3BYYNO4C187BG"

