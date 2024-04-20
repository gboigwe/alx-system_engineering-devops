#Using Puppet, install flask from pip3
import python
import python::devel

file { 'flask':
    ensure   => installed,
    provider => 'pip3',
    require  => Class['python::devel'],
}