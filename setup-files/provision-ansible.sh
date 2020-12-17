# Intalls Ansible
sudo apt-get update
sudo apt-get install software-properties-common -y
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get install ansible -y

# Installing python3 venv -- the recommended package to create virtual environments
sudo apt-get install python3-venv -y

# Makes a Downloads folder to allow the app to run
mkdir ~/Downloads

# Will setup up the Ansible hosts as needed
sudo mv /etc/ansible/hosts /etc/ansible/hosts.default
sudo ln -s ~/ansible-files/setup-files/hosts /etc/ansible/hosts