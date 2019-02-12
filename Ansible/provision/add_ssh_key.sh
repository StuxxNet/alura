RESULT=$(dpkg -l python)
if [[ ${?} -ne 0 ]]; then
    echo "Updating repositories"
    INSTALL=$(sudo apt-get update 2>&1)
    if [[ ${?} -ne 0 ]]; then
        echo "Error during update of the repos: ${INSTALL}" 1>&2
        exit 1
    else
        echo "Repositories updated"
    fi
    INSTALL=$(sudo apt-get install python -y 2>&1)
    if [[ ${?} -ne 0 ]]; then
        echo "Error during the installation of Python: ${INSTALL}" 1>&2
        exit 2
    else
        echo "Python successfully installed"
        INSTALL=$(cat /vagrant/provision/keys/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys 2>&1)
        if [[ ${?} -ne 0 ]]; then
            echo "Failed to copy the SSH key: ${INSTALL}" 1>&2
            exit 1
        else
            echo "Copied the public SSH key successfully"
            INSTALL=$(sudo chown vagrant:vagrant -R /home/vagrant/.ssh 2>&1)
            if [[ ${?} -ne 0 ]]; then
                echo "Failed to copy the SSH key: ${INSTALL}" 1>&2
                exit 5
            else
                echo "Changed the ownership of the .ssh folder"
            fi
        fi
    fi
else
    echo "Python already installed"
fi