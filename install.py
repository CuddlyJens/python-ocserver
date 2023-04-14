import os
# Enable the Recommendet Apache Modules
os.system('a2enmod dir env headers mime rewrite setenvif')
os.system('systemctl restart apache2')
print('done')
# Installation ownCloud
os.system("wget https://download.owncloud.com/server/stable/owncloud-complete-latest.tar.bz2 && \
tar -xjf owncloud-complete-latest.tar.bz2 && \
chown -R www-data. owncloud")