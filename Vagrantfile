Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.network "private_network", ip: "192.168.10.100"
  config.vm.provision "shell", path: "setup-files/provision-ansible.sh"
end
