#Using Puppet, install flask from pip3
class { 'python' }

package { 'python-devel':
    ensure => installed,
}
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Class['python::devel'],
}