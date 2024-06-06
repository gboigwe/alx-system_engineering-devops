# The Puppet manifest fixing Apache 500 error in WordPress

# Install required packages
package { 'apache2':
  ensure => present,
}

package { 'libapache2-mod-php':
  ensure  => present,
  require => Package['apache2'],
}

# Enable required Apache modules
apache2mod { 'php5':
  ensure  => present,
  require => Package['libapache2-mod-php'],
}

# Update WordPress configuration
exec { 'fix-wordpress':
  command => 'sed -i "s/.*DBPassword.*/define(\'DB_PASSWORD\', \'$(cat /root/.wp-pass)\');/" /var/www/html/wp-config.php',
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Package['libapache2-mod-php'],
  notify  => Service['apache2'],
}

# Ensure Apache service is running
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Apache2mod['php5'],
}
