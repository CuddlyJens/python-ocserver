import os
# Enable the Recommendet Apache Modules
os.system('a2enmod dir env headers mime rewrite setenvif')
os.system('systemctl restart apache2')
print('done')
# Installation ownCloud
os.system("cd /var/www/")
os.system("wget https://download.owncloud.com/server/stable/owncloud-complete-latest.tar.bz2 && \
tar -xjf owncloud-complete-latest.tar.bz2 && \
chown -R www-data. owncloud")
os.system('occ maintenance:install \
    --database "mysql" \
    --database-name "owncloud" \
    --database-user "owncloud" \
    --database-pass "testcloud" \
    --data-dir "/var/www/owncloud/data" \
    --admin-user "admin" \
    --admin-pass "admin"')