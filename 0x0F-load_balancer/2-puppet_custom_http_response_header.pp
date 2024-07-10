#automate the task of creating a custom HTTP header response, but with Puppet
# custom HTTP header must be X-Served-By


exec { 'update':
        command => '/usr/bin/apt-get update',
}

-> package { 'nginx':
	ensure => 'present',
}

-> file {'http_header':
	path => '/etc/nginx/nginx.conf',
	match => 'http {',
	line => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

-> exec {'redirect_me':
	command => '/usr/sbin/service nginx restart',
	provider => 'shell'
}
