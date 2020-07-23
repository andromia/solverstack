# general
apt-get update -y
apt-get upgrade -y
apt-get dist-upgrade -y
apt-get install build-essential -y
apt-get install -y git vim curl

# python3
apt-get install -y python3-dev python3-wheel python3-setuptools python3-six python3-pip

# rust
echo 'curl https://sh.rustup.rs -sSf | sh -s -- -y;' | su vagrant

# yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get -y update && sudo apt-get -y install yarn