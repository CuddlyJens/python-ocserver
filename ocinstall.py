import os

# # update system
# os.system('apt update && apt upgrade -y')

# # install Required and Recommended Packages, Configure Apache
# os.system('sudo add-apt-repository ppa:ondrej/php -y')
# os.system('sudo apt update && sudo apt upgrade -y')
# os.system('apt install -y \
#   apache2 \
#   libapache2-mod-php7.4 \
#   mariadb-server openssl redis-server wget \
#   php7.4 php7.4-imagick php7.4-common php7.4-curl \
#   php7.4-gd php7.4-imap php7.4-intl php7.4-json \
#   php7.4-mbstring php7.4-gmp php7.4-bcmath php7.4-mysql \
#   php7.4-ssh2 php7.4-xml php7.4-zip php7.4-apcu \
#   php7.4-redis php7.4-ldap php-phpseclib')
# os.system('apt-get install -y php7.4-smbclient')
# os.system('echo "extension=smbclient.so" > /etc/php/7.4/mods-available/smbclient.ini')
# os.system('phpenmod smbclient')
# os.system('systemctl restart apache2')
# os.system('apt install -y \
#   unzip bzip2 rsync curl jq \
#   inetutils-ping  ldap-utils\
#   smbclient')

with open('/etc/apache2/sites-available/owncloud.conf', 'w') as file:

    VHC = [
        "<VirtualHost *:80>",
        "# uncommment the line below if variable was set",
        "#ServerName \$my_domain",
        "DirectoryIndex index.php index.html",
        "DocumentRoot /var/www/owncloud",
        "<Directory /var/www/owncloud>",
        "  Options +FollowSymlinks -Indexes",
        "  AllowOverride All",
        "  Require all granted",
        " ",
        " <IfModule mod_dav.c>",
        "  Dav off",
        " </IfModule>",
        " ",
        " SetEnv HOME /var/www/owncloud",
        " SetEnv HTTP_HOME /var/www/owncloud",
        "</Directory>",
        "</VirtualHost>",
    ]

    file.writelines(VHC)
