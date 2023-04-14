import mysql.connector

owncloud = mysql.connector.connect(
    host="localhost",
    user="owncloud",
    passwd="testcloud",
)

mycursor = owncloud.cursor()
mycursor.execute("CREATE DATABASE owncloud")
mycursor.execute("GRANT ALL PRIVILEGES ON owncloud.* TO 'owncloud'@'localhost' IDENTIFIED BY 'testcloud'")
mycursor.execute("FLUSH PRIVILEGES")

print('run "python3 python-ocserver/install.py"')