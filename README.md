# Joomla 2.5 - 3.5 User Migrator
 This program will help you merge a joomla 2.5 users table with a joomla 3.5 users table.
- The results will be written to the joomla 3.5 table all usernames and emails will be checked.
- There will not be any overlapping results new entries will be written with auto-incrementing ids
- All new users will have a default password of "password123456!" - Have users change their password!
- All new users will be added as "registered" users.
 
# Instructions
- ONLY WORKING ON MYSQL 5.5.x
- MAKE A BACKUP OF YOUR 2 DATABASES! DON'T BE STUPID!
- setup the db.py file to match your 2 databases
- check the sqlQueries.py file to make sure you are querying the correct tables
- check the sqlQueries.py file to make sure you are INSERTING into the correct table
- run
- profit

# Dependencies

Python 3.5x

    sudo apt-get install python3-dev
    sudo apt install python3-pip

# Libraries

- csv

    pip install csv (deprecated)

- mysql-client

    pip install mysqlclient

- MySQLdb

    pip install MySQLdb (deprecated)

- datetime

    pip install datetime (part of standard library)


