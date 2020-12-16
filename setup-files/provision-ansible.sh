# Use this to install Ansible
sudo apt-get update
sudo apt-get install software-properties-common -y
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get install ansible -y

# Installing venv support
sudo apt-get install python3-venv

# Installing pip3 and app dependencies
# sudo apt-get install python-pip -y
# sudo apt-get install python-bs4 -y
# sudo apt-get install python3-pytest -y
# sudo apt-get install python-logilab-common -y
# sudo apt-get install python3-virtualenv -y
# pip3 install bs4
# pip3 install pytest

# Making a directory for the files to be downloaded to
# mkdir ~/Downloads
# chmod 777 ~/Downloads

# Installing pip
# sudo apt-get install python3-pip -y
# sudo apt-get install python3-venv -y

# python3 -m venv venv
# pip install pytest, bs4, requests