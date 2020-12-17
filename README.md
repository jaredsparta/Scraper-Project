# Web scraping app using Python

## Contents
1. [Creating a development environment](https://github.com/jaredsparta/Scraper-Project#Dev-Environments)

<br>

## Dev Environments
- As Ansible does not work on Windows machines, we can use a virtual machine to run Ubuntu and install Ansible there. It follows that we can use Vagrant boxes as an easy way to do this.
    - Within `setup-files` there is a `Vagrantfile` that can be used to create a provisioned Ubuntu VM
    - It is advised to use a Python virtual environment and you can create one using the Python package `venv` with `python3 -m venv <name-of-venv>`
    - To install the necessary Python packages within the virtual environment, you can simply run `python3 -m pip install -r requirements.txt`

- All the necessary provisioning is achieved using `setup-files/provision-ansible.sh` which runs when you `vagrant up` using the Vagrantfile given
    - If you want to install more dependencies, please do append this provision file how you see fit

<br>

## CI/CD - Continuous Integration and Deployment

- We will make use of Jenkins to automate the building, testing and deploying of pushed code into an EC2 instance.

- To ensure that the Python environment is standardised throughout, we will make use of a virtual environment created through the Python package `venv`
    - Within this environment, we can install all the necessary dependencies through `python3 -m pip install -r setup-files/requirements.txt`
    - This will allow the tests to run with the minimum number of dependencies and will avoid any packages that might ruin it

<br>