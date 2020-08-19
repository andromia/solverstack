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

    # web
    config.vm.network :forwarded_port, guest: 3000, host: 3000

    # route
    config.vm.network :forwarded_port, guest: 5000, host: 5000

    # crud
    config.vm.network :forwarded_port, guest: 5001, host: 5001

    # crud postgreSQL db
    config.vm.network :forwarded_port, guest: 5002, host: 5002

    # depot
    config.vm.network :forwarded_port, guest: 5003, host: 5003

    # geocode
    config.vm.network :forwarded_port, guest: 5004, host: 5004

    # queue
    config.vm.network :forwarded_port, guest: 7878, host: 7878

    # user
    config.vm.network :forwarded_port, guest: 8080, host: 8080

    # user-crud mongo db
    config.vm.network :forwarded_port, guest: 27017, host: 27017

    config.vm.provision "shell", path: SCRIPT
  end
