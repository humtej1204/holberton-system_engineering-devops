# Fix error found, Apache is returning a 500 error.
exec { 'fixing error':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
