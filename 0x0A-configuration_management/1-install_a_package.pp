#Using Puppet, install flask from pip3
import python
import python::devel

file { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Class['python::devel'],
}