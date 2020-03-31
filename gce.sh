# Install Stackdriver logging agent
curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh
sudo bash install-logging-agent.sh

# Install or update needed software(git, python, pip, virtualenv)
apt-get update
apt-get install -yq git python python-pip
pip install --upgrade pip virtualenv

# Install cloud_sql_proxy。指定目錄(-O)
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O /usr/local/bin/cloud_sql_proxy
chmod +x /usr/local/bin/cloud_sql_proxy

# 新增使用者pythonapp。自動建立家目錄(-m)，指定家目錄(-d)
# useradd -m -d /home/pythonapp pythonapp

# Fetch source code
export HOME=/root
# git clone -b f_CreateDeployment --single-branch https://github.com/reddtsai/pythonLotteryScraper.git /opt/app
git clone https://github.com/reddtsai/pythonLotteryScraper.git /opt/app

# Python environment setup
virtualenv -p python3 /opt/app/gce/env
source /opt/app/gce/env/bin/activate
/opt/app/gce/env/bin/pip install -r /opt/app/requirements.txt

# Setup cloud_sql_proxy on system service
cp /opt/app/cloud-sql-proxy.service /etc/systemd/system/cloud-sql-proxy.service
systemctl enable cloud-sql-proxy.service
systemctl start cloud-sql-proxy.service

sleep 15

# Scheduling scraper on system service
cp /opt/app/lotto-scraper.service /etc/systemd/system/lotto-scraper.service
systemctl enable lotto-scraper.service
systemctl start lotto-scraper.service
cp /opt/app/lotto-scraper.timer /etc/systemd/system/lotto-scraper.timer
systemctl enable lotto-scraper.timer
systemctl start lotto-scraper.timer

# 設定擁有者:群組。目錄下所有子目錄和檔案(-R)
# chown -R pythonapp:pythonapp /opt/app