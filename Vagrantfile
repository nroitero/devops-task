# -*- mode: ruby -*-
# vi: set ft=ruby :

def ensure_plugins(plugins)
  logger = Vagrant::UI::Colored.new
  result = false
  plugins.each do |p|
    pm = Vagrant::Plugin::Manager.new(
      Vagrant::Plugin::Manager.user_plugins_file
    )
    plugin_hash = pm.installed_plugins
    next if plugin_hash.has_key?(p)
    result = true
    logger.warn("Installing plugin #{p}")
    pm.install_plugin(p)
  end
  if result
    logger.warn('Re-run vagrant up now that plugins are installed')
    exit
  end
end
ensure_plugins(["vagrant-vbguest","vagrant-hostsupdater","vagrant-cachier"])
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vbguest.auto_update = false
  config.vm.box_check_update = false
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.inventory_path = "inventory"
    ansible.limit = 'vagrant'
  end
  config.vm.hostname ="devops-task.test"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.provider "virtualbox" do |vb|
    vb.cpus = "1"
    vb.name = "devops-task"
    vb.memory = "4096"
  end
end
