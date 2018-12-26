exec {"apt-update":
  command => "apt-get update",
  path => "/usr/bin"
}

package {"mariadb-server":
  ensure => installed,
  require => Exec["apt-update"]
}

service {"mariadb":
  ensure => running,
  enable => true,
  hasstatus => true,
  hasrestart => true,
  require => Package["mariadb-server"]
}

exec {"mysql-create-db":
  command => "mysqladmin -uroot create musicjungle",
  unless => "mysql -uroot musicjungle",
  path => "/usr/bin",
  require => Service["mariadb"]
}

exec {"create-user":
  command => "mysql -uroot -e \"GRANT ALL PRIVILEGES ON * TO 'musicjungle'@'%' IDENTIFIED BY 'av2f8bv8';\" musicjungle",
  path => "/usr/bin",
  onlyif => "mysql -uroot musicjungle",
  require => Service["mariadb"]
}

file {"/etc/mysql/my.cnf":
  source => "/vagrant/manifests/configs/my.cnf",
  owner => root,
  group => root,
  mode => "0644",
  require => Package["mariadb-server"],
  notify => Service["mariadb"]
}
