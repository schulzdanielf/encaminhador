Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 4
  end


  config.vm.define "ubuntu_server1" do |ubuntu_server1|
    ubuntu_server1.vm.network "forwarded_port", guest: 8888, host: 8888
    ubuntu_server1.vm.network "public_network", ip: "192.168.1.110"
    ubuntu_server1.vm.synced_folder "./configs", "/configs"


    ubuntu_server1.vm.provision "shell",
      inline: "apt-get update && apt-get install -y puppet"

    ubuntu_server1.vm.provision "shell",
      inline: "cat /vagrant/configs/id_ubuntu.pub >> .ssh/authorized_keys"
  #  ubuntu_server1.vm.provision "puppet" do |puppet|
  #    puppet.manifests_path = "./configs/manifests"
  #    puppet.manifest_file = "phpweb.pp"
  #  end
  end

  config.vm.define "ubuntu_server2" do |ubuntu_server2|
    ubuntu_server2.vm.network "forwarded_port", guest: 8889, host: 8889
    ubuntu_server2.vm.network "public_network", ip: "192.168.1.111"
    ubuntu_server2.vm.synced_folder "./configs", "/configs"

    ubuntu_server2.vm.provision "shell",
      inline: "apt-get update && apt-get install -y puppet"
    ubuntu_server2.vm.provision "shell",
      inline: "cat /vagrant/configs/id_ubuntu.pub >> .ssh/authorized_keys"

  #  phpweb.vm.provision "puppet" do |puppet|
  #    puppet.manifests_path = "./configs/manifests"
  #    puppet.manifest_file = "phpweb.pp"
    end

    config.vm.define "ansible" do |ansible|
      ansible.vm.network "public_network", ip: "192.168.1.26"
      ansible.vm.synced_folder "./configs", "/configs"

      ansible.vm.provision "shell",
        inline: "cp /vagrant/id_ubuntu  /home/vagrant && \
                chmod 600 /home/vagrant/id_ubuntu && \
                chown vagrant:vagrant /home/vagrant/id_ubuntu"

      ansible.vm.provision "shell",
        inline: "apt-get update && \
                 apt-get install -y software-properties-common && \
                 apt-get install -y ansible"

       ansible.vm.provision "shell",
         inline: "ansible-playbook --private-key id_ubuntu -i /vagrant/configs/ansible/hosts /vagrant/configs/ansible/playbook.yml"
    end
  end
