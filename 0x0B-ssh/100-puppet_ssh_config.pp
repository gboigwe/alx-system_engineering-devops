# Using Puppet to make changes to configuration file
# so that I can connect to a server without typing a password

file { '/etc/ssh/ssh_config':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => @("EOF")
# Configuration of ssh using puppet
Host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	EOF
}
