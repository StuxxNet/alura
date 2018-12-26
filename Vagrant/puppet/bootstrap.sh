#!/bin/bash
apt-get update && apt-get -y install puppet && puppet module install puppetlabs-apache && puppet module install puppetlabs-stdlib --version 5.1.0

echo "Puppet installed!"
