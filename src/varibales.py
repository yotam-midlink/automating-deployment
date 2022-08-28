# test vars (change instance and path)

turn_to_prod_comment = "cd /home/ec2-user ; sed -e \"/^define('WP_HOME','https:\/\/backup.campus.gov.il'/s/^/\/\/ /\" -i wp-config.php; sed -e \"/^define('WP_SITEURL','https:\/\/backup.campus.gov.il'/s/^/\/\/ /\" -i wp-config.php"
turn_to_prod_uncomment = "cd /home/ec2-user ; sed -e \"/^\/\/ define('WP_HOME','https:\/\/campus.gov.il'/s/^\/\/ //g\" -i wp-config.php; sed -e \"/^\/\/ define('WP_SITEURL','https:\/\/campus.gov.il'/s/^\/\/ //g\" -i wp-config.php"

turn_to_backup_comment = "cd /home/ec2-user ; sed -e \"/^define('WP_HOME','https:\/\/campus.gov.il'/s/^/\/\/ /\" -i wp-config.php; sed -e \"/^define('WP_SITEURL','https:\/\/backup.campus.gov.il'/s/^/\/\/ /\" -i wp-config.php"
turn_to_backup_uncomment = "cd /home/ec2-user ; sed -e \"/^\/\/ define('WP_HOME','https:\/\/backup.campus.gov.il'/s/^\/\/ //g\" -i wp-config.php; sed -e \"/^\/\/ define('WP_SITEURL','https:\/\/campus.gov.il'/s/^\/\/ //g\" -i wp-config.php"