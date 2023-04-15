# python-ocserver
# Introduction
This is an (almost completely) Python Script to install the ownCloud Server on a fresh installation of Ubuntu 22.04. Run the following commands in your terminal to complete the installation.
```
sudo git clone https://github.com/CuddlyJens/python-ocserver.git
```
```
sudo python3 python-ocserver/prep.py
```
# In the MySQL Installer
## Insert Root Password
## Switch to unix_socket authentication [Y/n]
no
## Change the root password? [Y/n]
no
## Remove anonymous users? [Y/n]
yes
## Disallow root login remotely? [Y/n]
yes
## Remove test database and access to it? [Y/n]
yes
## Reload privilege tables now? [Y/n]
yes
```
reboot
```
# After reboot
## Login with root
## Login mysql
```
mysql -u root -p
```
## Create Database
```
CREATE DATABASE [name-of-database];
```
## Create a user
```
CREATE USER 'exampleuser'@'localhost' IDENTIFIED BY 'YourStrongPassword';
```
## Grant Privileges
```
GRANT ALL PRIVILEGES ON [name-of-database].* TO 'exampleuser'@'localhost' IDENTIFIED BY 'YourStrongPassword';
```
## Flush the Privileges
```
FLUSH PRIVILEGES;
```
## Quit out
```
quit;
```
# Finish the Installation
```
sudo python3 python-ocserver/install.py
```
# Open your Browser and insert your IP Adress from your Ubuntu Server
Create your Admin Account. 
Make sure to insert your correct Database-Username, -Password and Database-Name. If you didn't change your Database location, you gonna use 'localhost' as it is in default mode.
#
Complete the installation and log in with the admin credentials you created.
