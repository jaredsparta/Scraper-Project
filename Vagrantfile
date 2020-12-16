Vagrant.configure("2") do |config|
  config.vm.define "controller" do |controller|
    controller.vm.box = "ubuntu/xenial64"
    controller.vm.network "private_network", ip: "192.168.10.100"
    controller.vm.provision "shell", path: "setup-files/provision-ansible.sh"
    controller.vm.synced_folder ".", "/home/vagrant/Scraper"
  end
end
