# Install and configure an Nginx server
package { 'nginx':
 ensure  => installed,
 command => 'sudo apt install nginx -y',
}
exec { 'configuration':
  provider => shell,
  command  => ['sudo chown -R ubuntu /var/www',
              'echo "Hellow World" > /var/www/html/index.nginx-debian.html',
              'sudo sed -i "53i\ \n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=_WRBAzV-iHI&t=1s}\n" /etc/nginx/sites-available/default',
              'sudo service nginx restart'],
}
