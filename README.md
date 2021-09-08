# OSRS Sqlite3 Item Database
 This project creates an sqlite database containing all items presented in the [OSRSBox item database](https://github.com/osrsbox/osrsbox-db) 

This project is very rough and does not contain all properties of items in OSRSBox, for example it does not contain details on stance information or requirements until I can figure out how to model that properly in a database.
## Example data

* Here is the first few items of the database alongside a few available properties for each item  
![image](https://user-images.githubusercontent.com/55999153/132579233-dff69b33-4526-4c11-bead-0dd622925d27.png)

## Steps to run code ##
* Python >= 3.6 is required for osrs-db
* make sure [osrs-db](https://pypi.org/project/osrsbox/) is installed `pip install osrsbox`
* instructions for getting sqlite installed can be found [here](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
* run main.py  `python install osrsbox` if your default python version for `python` command is not >= 3.6 then use `python3 install osrsbox` instead
* all tables should now be present in OSRSItems.db which can be imported into some software or be accessed through usual sqlite CLI commands
