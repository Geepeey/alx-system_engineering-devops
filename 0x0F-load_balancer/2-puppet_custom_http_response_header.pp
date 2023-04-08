# A Puppet manifest that sets up an Nginx web server on a server
# It adds a custom HTTP header with Puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Holberton School',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  require => Package['nginx'],
}


file_line { 'addHeader':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $hostname;',
  require => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

