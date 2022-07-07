<?php
/** Enable W3 Total Cache */
define('WP_CACHE', true); // Added by W3 Total Cache

/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// define('DB_NAME', $_ENV['RDS_DB_NAME']);
// define('DB_USER', $_ENV['RDS_USERNAME']);
// define('DB_HOST', $_ENV['RDS_HOSTNAME'] . ':' . $_ENV['RDS_PORT']);
// define('DB_HOST_READER', $_ENV['RDS_HOSTNAME_READER'] . ':' . $_ENV['RDS_PORT']);
// define('WP_SITEURL', $_ENV['WP_URL']); 
// define('WP_HOME', $_ENV['WP_URL']); 
// define('WP_MEMORY_LIMIT', '32M');

///****** */ This config belong to BACKUP environment *****/////

/** The name of the database for WordPress */
define('WP_HOME','https://backup.campus.gov.il');
define('WP_SITEURL','https://backup.campus.gov.il');

// define('WP_HOME','https://campus.gov.il');
// define('WP_SITEURL','https://campus.gov.il');

$_SERVER['HTTPS'] = 'on';

// ** MySQL settings - You can get this info from your web host ** //
// #define('DB_NAME', 'campus');
define('DB_NAME', 'campus');

// /** MySQL database username */
define('DB_USER', 'dbmaster');

// /** MySQL hostname */
define('DB_HOST', 'backup-production-ecs-cluster-cluster.cluster-camrroswumcd.eu-west-1.rds.amazonaws.com');

/** MySQL database password */
define('DB_PASSWORD', '12dbmaster34');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'put your unique phrase here');
define('SECURE_AUTH_KEY',  'put your unique phrase here');
define('LOGGED_IN_KEY',    'put your unique phrase here');
define('NONCE_KEY',        'put your unique phrase here');
define('AUTH_SALT',        'put your unique phrase here');
define('SECURE_AUTH_SALT', 'put your unique phrase here');
define('LOGGED_IN_SALT',   'put your unique phrase here');
define('NONCE_SALT',       'put your unique phrase here');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';


/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* To fix unable to install plugins issue */
define('FS_METHOD', 'direct');

// if (strpos($_SERVER['HTTP_X_FORWARDED_PROTO'], 'https') !== false)
//     $_SERVER['HTTPS']='on';

// if (isset($_SERVER['HTTP_CLOUDFRONT_FORWARDED_PROTO'])
//   && $_SERVER['HTTP_CLOUDFRONT_FORWARDED_PROTO'] === 'https') {
//   $_SERVER['HTTPS'] = 'on';
// }

// if (strpos($_SERVER['HTTP_CLOUDFRONT_FORWARDED_PROTO'], 'https') !== false)
//     $_SERVER['HTTPS']='on';

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');

