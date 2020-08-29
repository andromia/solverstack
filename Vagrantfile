# -*- mode: ruby -*-
# vi: set ft=ruby :


PROVIDER = "virtualbox"
BOX = "bento/ubuntu-20.04"
SCRIPT = "./scripts/vm-bootstrap.sh"

# if on windows host without admin rights, warn & exit
if Vagrant::Util::Platform.windows? then
  def running_in_admin_mode?
    (`reg query HKU\\S-1-5-19 2>&1` =~ /ERROR/).nil?
  end

  unless running_in_admin_mode?
    puts "This vagrant makes use of SymLinks to the host. On Windows, Administrative privileges are required to create symlinks (mklink.exe). Try again from an Administrative command prompt."
    exit 1
  end
end

Vagrant.configure(2) do |config|

    config.vm.provider PROVIDER do |vb|
      vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
    end

    # config.vm.synced_folder ".", "/var/www", type: "rsync", rsync__args: ["--verbose", "--archive", "--delete", "-z"]

    config.vm.box = BOX

    # Install Docker
    config.vm.provision :docker

    # Install Docker Compose
    # First, install required plugin https://github.com/leighmcculloch/vagrant-docker-compose:
    # vagrant plugin install vagrant-docker-compose
    config.vm.provision :docker_compose

    # NOTE: service ports will be managed by docker for prod

    # web
    config.vm.network :forwarded_port, guest: 3000, host: 3000

    # route
    config.vm.network :forwarded_port, guest: 5000, host: 5000

    # geocode
    config.vm.network :forwarded_port, guest: 5001, host: 5001

    # depot
    config.vm.network :forwarded_port, guest: 5002, host: 5002

    # user
    config.vm.network :forwarded_port, guest: 5003, host: 5003

    # crud
    config.vm.network :forwarded_port, guest: 5004, host: 5004

    # crud postgreSQL db
    config.vm.network :forwarded_port, guest: 5006, host: 5006

    config.vm.provision "shell", path: SCRIPT
  end
