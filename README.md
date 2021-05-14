# OSRS Sqlite3 Item Database
 This project creates an sqlite database containing all items presented in the [OSRSBox item database](https://github.com/osrsbox/osrsbox-db) 

This project is very rough and does not contain all properties of items in OSRSBox, for example it does not contain details on stance information or requirements until I can figure out how to model that properly in a database.

## Steps to run code ##
* make sure osrs-db is downloaded from pypi
* sqlite3 must also be installed also probably through pip
* run main.py
* all tables should now be present in OSRSItems.db which can be imported into some software or seen in sqlite CLI command
