sudo systemctl start mongod
sudo systemctl status mongod



sudo ufw allow from 172.17.151.47/32 to any port 27017

sudo ufw status