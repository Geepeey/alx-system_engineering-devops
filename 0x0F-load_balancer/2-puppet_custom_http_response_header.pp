# Install Nginx and update apt-get packages
apt::update { 'update':
  before => Class['nginx'],
}

class { 'nginx': }

# Add a custom HTTP header to Nginx configuration file
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "add_header X-Served-By \"${::hostname}\";",
  match => 'http {',
  require => Class['nginx'],
}

# Restart the Nginx service after modifying its configuration
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => [File_line['http_header']],
  require    => Class['nginx'],
}
