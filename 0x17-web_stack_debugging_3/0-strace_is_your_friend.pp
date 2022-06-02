# Fix error found, Apache is returning a 500 error.
file_line { 'fix Apache error':
  ensure => 'present',
  path   => '/var/www/html/wp-settings.php',
  line   => "require( ABSPATH . WPINC . '/class-wp-error.php' );",
  match  => "require( ABSPATH . WPINC . '/class-wp-error.phpp' );",
}
