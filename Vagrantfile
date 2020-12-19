Vagrant.configure("2") do |config|
  config.vm.define "controller" do |controller|
    controller.vm.box = "ubuntu/bionic64"
    controller.vm.network "private_network", ip: "192.168.10.100"
    controller.vm.provision "shell", path: "vagrant-setup/provision-ansible.sh"
    controller.vm.synced_folder "ansible-files", "/home/vagrant/ansible-files"
    controller.vm.synced_folder "DevOpsProject-ItJobsWatch-master", "/home/vagrant/DevOpsProject-ItJobsWatch-master"
  end
end
