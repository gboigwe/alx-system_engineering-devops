# Configure the system-wide SSH client configuration
#
# Requirements:
#   - Use the private key /home/school/.ssh/school
#   - Disable password authentication

file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => @("END_CONFIG"/),
    # Use the private key /home/school/.ssh/school
    IdentityFile /home/school/.ssh/school

    # Disable password authentication
    PasswordAuthentication no
    END_CONFIG
}
