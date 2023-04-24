# This puppet manifest installs and configures nginx server
exec {'update':
  command => 'apt-get -y update',
  path    => '/usr/bin',
}

package {'nginx':
  ensure   => 'installed',
  name  => 'nginx',
  provider => 'apt',
}

file {'html':
  ensure  => 'present',
  path    => '/var/www/html/index.nginx-debian.html',
  content => "Hello World!\n",
}

file {'Error_404':
  ensure  => 'present',
  path    => '/usr/share/nginx/html/custom_404.html',
  content => "Ceci n\'est pas une page\n",
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

exec {'configure':
  command => 'sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/micoliser permanent;\n\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html {\n\t\troot \/usr\/share\/nginx\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-available/default',
  path    => '/usr/bin',
}

exec {'restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => Service['nginx'],
}
