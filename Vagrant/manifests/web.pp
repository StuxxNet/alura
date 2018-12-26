exec { "apt-update":
  command => "apt-get update",
  path => "/usr/bin"
}

package { ["openjdk-8-jre", "tomcat8"]:
    ensure => installed,
    require => Exec["apt-update"]
}

service { "tomcat8": 
  ensure => running,
  enable => true,
  hasstatus => true,
  hasrestart => true,
  require => Package["tomcat8"]
}

file { "/var/lib/tomcat8/webapps/musicjungle.war":
  source => "/vagrant/manifests/war/vraptor-musicjungle.war",
  owner => tomcat8,
  group => tomcat8,
  mode => "0644",
  require => Package["tomcat8"],
  notify => Service["tomcat8"]
} -> exec {"wait_for_my_web_service":
  command => "sleep 15",
  path => "/usr/bin:/bin",
} -> file { "/var/lib/tomcat8/webapps/musicjungle/WEB-INF/classes/META-INF/persistence.xml":
  source => "/vagrant/manifests/configs/persistence.xml",
  owner => tomcat8,
  group => tomcat8,
  mode => "0644",
  require => Package["tomcat8"],
  notify => Service["tomcat8"]
}

file_line { "prodution":
  path => "/etc/default/tomcat8",
  line => "JAVA_OPTS=\"\$JAVA_OPTS -Dbr.com.caelum.vraptor.environment=production\"",
  require => Package["tomcat8"],
  notify => Service["tomcat8"]
}
