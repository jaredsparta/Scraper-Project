# Web scraping app using Python

- A full project that will create a development, testing and deployment environment for the app found in `DevOpsProject-ItJobsWatch-master`

- All the required infrastructure is created through Ansible playbooks

<br>

## Pre-requisites
- You will need the following software available on your machine:
    - `Git`
    - `Vagrant`


## Contents
1. [Creating a development environment](https://github.com/jaredsparta/Scraper-Project#Dev-Environments)
2. [CI/CD](https://github.com/jaredsparta/Scraper-Project#CICD-or-Continuous-Integration-and-Deployment)
3. [Ansible](https://github.com/jaredsparta/Scraper-Project#Ansible-to-create-the-Deployment-environment)
4. [Flask front-end](https://github.com/jaredsparta/Scraper-Project#Getting-the-Flask-app-running)

<br>

## Dev Environments
- We want a development environment that can be used both as an Ansible controller and 
    - Within `setup-files` there is a `Vagrantfile` that can be used to create a provisioned Ubuntu VM
    - It is advised to use a Python virtual environment and you can create one using the Python package `venv` with `python3 -m venv <name-of-venv>`
    - To install the necessary Python packages within the virtual environment, you can simply run `python3 -m pip install -r requirements.txt`

- All the necessary provisioning is achieved using `setup-files/provision-ansible.sh` which runs when you `vagrant up` using the Vagrantfile given
    - If you want to install more dependencies, please do append this provision file how you see fit

- In some cases, the provision file may fail to install the necessary dependencies for Ansible, in such a case just run the command `python -m pip install -r ~/ansible-files/setup-files/requirements.txt` within the VM

<br>

[Back to top](https://github.com/jaredsparta/Scraper-Project#Contents)

## CI/CD or Continuous Integration and Deployment

- We will make use of Jenkins to automate the building, testing and deploying of pushed code into an EC2 instance.

- To ensure that the Python environment is standardised throughout, we will make use of a virtual environment created through the Python package `venv`
    - Within this environment, we can install all the necessary dependencies through `python3 -m pip install -r setup-files/requirements.txt`
    - This will allow the tests to run with the minimum number of dependencies and will avoid any packages that might ruin it

<br>

[Back to top](https://github.com/jaredsparta/Scraper-Project#Contents)

## Ansible to create the Deployment environment
- Things to note:
    1. Ansible will use Python2 by default, you will need to download the necessary Python dependencies for modules to run using `python -m pip install` as opposed to `python3 -m pip install`
    2. If you are intent on Ansible using Python3 then an easy way to do so is explicitly calling it when you run a playbook. For example, `ansible-playbook example-playbook.yml -e 'ansible_python_interpreter=/usr/bin/python3'` will use Python3 as the interpreter
        - If doing so, ensure that you have correctly installed the necessary dependencies

- We will make use of Ansible playbooks and run them on the vagrant machine as the controller

- The AWS access and secret keys is sensitive information and will need to be secured properly. We can make use of Ansible vaults for such a task. The vault (which is really a password-protected YAML file) should be kept in `ansible-playbooks/group_vars/all/`
    1. Create a vault using `ansible-vault create ~/ansible-files/creating-infrastructure/group_vars/all/<name-of-vault>.yml`
        - I will name mine `aws_keys.yml`
        - Choose the password as you see fit
    2. Input the access and secret keys inside this file as well as your public IP address (for use in playbooks). It should look like the following

    ![](images/vault.jpg)
    
    3. To see what's inside the file after exiting you can `ansible-vault view aws_keys.yml`
    4. To edit the keys again you can `ansible-vault edit aws_keys.yml`

- Finally, to run playbooks with the use of ansible vaults, you can run `ansible-playbook <playbook-name>.yml --ask-vault-pass`

<br>

**Creating the VPC**

- In an effort to programmatically create infrastructure, we will make use of Ansible playbooks to create a VPC in which we will create an EC2 instance to deploy the app

- The following Ansible modules were used to write `create-vpc.yml`:
    1. `ec2_vpc_net`
    2. `community.aws.ec2_vpc_nacl`
    3. `community.aws.ec2_vpc_igw`
    4. `amazon.aws.ec2_vpc_subnet`
    5. `community.aws.ec2_vpc_route_table`

<br>

**Creating the deployment environment EC2 instance**

- Again, a more efficient method to creating instances is through Ansible. We will make use of playbooks to create EC2 instances within the newly-created VPC.

- The following Ansible modules were used to write `ec2-deployment-env.yml`:
    1. `community.aws.ec2_instance`
    2. `amazon.aws.ec2_group`

<br>

**Creating the playbook that would prepare the environment to run the app**

- Notes to be made:
    1. There was some issues with `scp` when copying in files via a Jenkins job, mainly that there were permissions error (i.e. the user that Jenkins SSH'ed into had no permission to change them). This was fixed by adding a line in the playbook that explicitly states the owner of the files to be copied as `ubuntu` -- the user Jenkins SSH's into the instance as

    ![](images/copy.jpg)

- I wrote this playbook to give me a way to deploy the app on a newly-created EC2 instance. It makes use of the following Ansible modules:
    1. `file`
    2. `apt`
    3. `copy`
    4. `service`
    5. `shell`
    6. `pip`
    7. `systemd`

- The playbook will: install the necessary packages; install the pip dependencies; create a virtal environment for the app to run; create a new system service for the app; reconfigure nginx as a reverse-proxy; and finally start the app

<br>

[Back to top](https://github.com/jaredsparta/Scraper-Project#Contents)

## Getting the Flask app running
- The main steps I took to ensure that the Flask front-end was implemented properly in a production environment were to do the following:
    1. Use nginx as a reverse-proxy to port 5000 (where my Flask app was running)
    2. Use `gunicorn` as the server for Flask to run on
    3. Created a system service that would allow me to restart the Flask app, similar to how nginx is restarted etc.

- The system service was created in `/etc/systemd/system/` and had the following information:

![](images/service.jpg)

<br>

**Writing the actual Flask code**

- Very little refactoring of code was done. For the ones that were refactored, nothing was removed but some functions were just added:
    1. Created another python file that did the exact same thing as the app but without user input (so all it would do is insert a `.csv` file into the `~/Downloads` folder)
    2. When it downloaded, I wrote a function that would read in the `.csv` and parse the information into a dictionary which I could parse again into an HTML file using Jinja2 syntax (exactly like variable substituting in Ansible playbooks)
    3. Then the rest of the front-end was simply Flask syntax, do read the comments written in `app.py` for more

- The main files that the Flask app uses are found in `DevOpsProject-ItJobsWatch-master`:
    1. `app.py` is the actual Flask app itself
    2. `templates/` are where the HTML files that Flask uses are kept
    3. `static/` contains all the images used in these HTML files
    4. `wsgi.py` is a Python script that imports the Flask app -- this was used to actually make the system service as shown above (this was preferable as changing the app meant I wouldn't have to reload the actual service file itself since `wsgi.py` remained unchanged)

[Back to top](https://github.com/jaredsparta/Scraper-Project#Contents)

<br>

---
**Used:**
- [Creating system services](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)