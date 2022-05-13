# Install and configure an Nginx server
exec { 'configuration':
  provider => shell,
  command  => ['sudo apt-get -y update', 'sudo apt-get -y install nginx',
              'sudo chown -R ubuntu /var/www',
              'echo "Hellow World" > /var/www/html/index.nginx-debian.html',
              'sudo sed -i "53i\ \n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=_WRBAzV-iHI&t=1s}\n" /etc/nginx/sites-available/default',
              'sudo service nginx restart'],
}
