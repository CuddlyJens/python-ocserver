import os
# update system
os.system('apt update && apt upgrade -y')
os.system('apt-get install nodejs -y')
os.system('npm install mysql')

os.system('FILE="/usr/local/bin/occ"')
os.system('cat <<EOM >/usr/local/bin/occ')
os.system('#! /bin/bash')
os.system('cd /var/www/owncloud')
os.system('sudo -E -u www-data /usr/bin/php /var/www/owncloud/occ "\$@"')
os.system('EOM')
os.system('chmod +x /usr/local/bin/occ')

# install Required and Recommended Packages, Configure Apache
os.system('sudo add-apt-repository ppa:ondrej/php -y')
os.system('sudo apt update && sudo apt upgrade -y')
os.system('apt install -y \
  apache2 \
  libapache2-mod-php7.4 \
  mariadb-server openssl redis-server wget \
  php7.4 php7.4-imagick php7.4-common php7.4-curl \
  php7.4-gd php7.4-imap php7.4-intl php7.4-json \
  php7.4-mbstring php7.4-gmp php7.4-bcmath php7.4-mysql \
  php7.4-ssh2 php7.4-xml php7.4-zip php7.4-apcu \
  php7.4-redis php7.4-ldap php-phpseclib')
os.system('apt-get install -y php7.4-smbclient')
os.system('echo "extension=smbclient.so" > /etc/php/7.4/mods-available/smbclient.ini')
os.system('phpenmod smbclient')
os.system('systemctl restart apache2')
os.system('apt install -y \
  unzip bzip2 rsync curl jq \
  inetutils-ping  ldap-utils\
  smbclient')

with open('/etc/apache2/sites-available/owncloud.conf', 'w') as file:

    VHC = [
        "<VirtualHost *:80>\n",
        "# uncommment the line below if variable was set\n",
        "#ServerName \$my_domain\n",
        "DirectoryIndex index.php index.html\n",
        "DocumentRoot /var/www/owncloud\n",
        "<Directory /var/www/owncloud>\n",
        "  Options +FollowSymlinks -Indexes\n",
        "  AllowOverride All\n",
        "  Require all granted\n",
        " \n",
        " <IfModule mod_dav.c>\n",
        "  Dav off\n",
        " </IfModule>\n",
        " \n",
        " SetEnv HOME /var/www/owncloud\n",
        " SetEnv HTTP_HOME /var/www/owncloud\n",
        "</Directory>\n",
        "</VirtualHost>\n",
    ]

    file.writelines(VHC)
    file.close


os.system('a2dissite 000-default')
os.system('a2ensite owncloud.conf')

# Install MySQL
os.system('mysql_secure_installation')
os.system('apt install -y python3-pip')
print('run "python3 -m install mysql-connector')
print('run "python3 python-ocserver/mysql.py"')