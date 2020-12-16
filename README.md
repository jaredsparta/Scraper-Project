# Web scraping app using Python

## Contents
1. [Creating a development environment](https://github.com/jaredsparta/Scraper-Project#Dev-Environments)

<br>

## Dev Environments
- We can create a development environment using Vagrant boxes. As Ansible does not work on Windows machines, we must use a virtual box with an Ubuntu box to do so.
    - The `Vagrantfile` included will be able to be used to do so.

- The `.venv` included within the repository is a virtual environment that can be used. What was installed:
    1. `python3 -m pip install bs4`
    2. `python3 -m pip install requests`
    3. `python3 -m pip install pytest`
    4. `python3 -m pip install requirements.txt`