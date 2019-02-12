RESULT=$(dpkg -l ansible)
if [[ ${?} -eq 1 ]]; then
    echo "Updating repositories"
    INSTALL=$(sudo apt-get update 2>&1)
    if [[ ${?} -ne 0 ]]; then
        echo "Error during update of the repos: ${INSTALL}" 1>&2
        exit 1
    else
        echo "Repositories updated"
    fi
    INSTALL=$(sudo apt-get install ansible -y 2>&1)
    if [[ ${?} -ne 0 ]]; then
        echo "Error during the installation of Ansible: ${INSTALL}" 1>&2
        exit 2
    else
        echo "Ansible successfully installed"
        INSTALL=$(sudo cp /vagrant/configs/hosts /etc/ansible/ 2>&1)
        if [[ ${?} -ne 0 ]]; then
            echo "Error during copy of the hosts file ${INSTALL}" 1>&2
            exit 3
        else
            echo "Hosts file copied successfully"
            INSTALL=$(sudo cp /vagrant/provision/keys/id_rsa /home/vagrant/.ssh 2>&1)
            if [[ ${?} -ne 0 ]]; then
                echo "Failed to copy the SSH key: ${INSTALL}" 1>&2
                exit 4
            else
                echo "Copied the private SSH key successfully"
                INSTALL=$(sudo chown vagrant:vagrant -R /home/vagrant/.ssh 2>&1)
                if [[ ${?} -ne 0 ]]; then
                    echo "Failed to copy the SSH key: ${INSTALL}" 1>&2
                    exit 5
                else
                    echo "Changed the ownership of the .ssh folder"
                fi
            fi
        fi
    fi
else
    echo "Ansible already installed"
fi