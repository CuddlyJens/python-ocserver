import os
import time
# Enable the Recommendet Apache Modules
os.system('a2enmod dir env headers mime rewrite setenvif')
os.system('systemctl restart apache2')
print('done')
# Installation ownCloud
os.chdir('/var/www/')
print("Current working directory: {0}".format(os.getcwd()))
time.sleep(2)
os.system('wget https://download.owncloud.com/server/stable/owncloud-complete-latest.tar.bz2 && \
tar -xjf owncloud-complete-latest.tar.bz2 && \
chown -R www-data. owncloud') 