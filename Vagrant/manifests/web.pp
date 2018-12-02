exec { "apt-get update":
    command => "/usr/bin/apt-get update"
}

package { ["openjdk-7-jre", "tomcat7", "unzip"]:
    ensure => installed,
    require => Exec["apt-get update"],
}