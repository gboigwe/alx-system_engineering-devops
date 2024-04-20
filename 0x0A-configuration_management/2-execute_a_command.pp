# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'pkill -f killmenow' }
