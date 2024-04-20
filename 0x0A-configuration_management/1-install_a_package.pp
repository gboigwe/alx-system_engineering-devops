#Using Puppet, install flask from pip3

exec {'pip3 install flask':
    require => Exec['python-installed'],
    command => '/usr/bin/pip3 install flask==2.1.9',
}

exec { 'python-installed':
    command => '/usr/bin/which python3'
}
