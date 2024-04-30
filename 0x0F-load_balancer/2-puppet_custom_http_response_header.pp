# Install and configure HTTP Response Header

exec { 'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.html ; echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html ; sudo sed -i "/server_name _/a add_header X-Server_By $HOSTNAME;" /etc/nginx/sites-enabled/default ; sudo nginx -t ; sudo service nginx restart',
}
