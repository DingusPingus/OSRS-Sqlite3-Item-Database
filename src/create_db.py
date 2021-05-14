import sqlite3

db = sqlite3.connect('OSRSItems.db')

db = db.cursor()

db.execute('''CREATE TABLE ItemsProperties(
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            last_updated TEXT NOT NULL,
            incomplete BOOLEAN NOT NULL,
            members BOOLEAN NOT NULL,
            tradeable BOOLEAN NOT NULL,
            tradeable_on_ge BOOLEAN NOT NULL,
            stackable BOOLEAN NOT NULL,
            stacked, INTEGER,
            noted BOOLEAN NOT NULL,
            noteable BOOLEAN NOT NULL,
            linked_id_item INTEGER,
            linked_id_noted INTEGER,
            linked_id_placeholder INTEGER,
            placeholder BOOLEAN NOT NULL,
            equipable_by_player BOOLEAN NOT NULL
            equipable_weapon BOOLEAN NOT NULL,
            cost INTEGER NOT NULL
            lowalch INTEGER,
            highalch INTEGER,
            weight FLOAT,
            buy_limit INTEGER,
            quest_item BOOLEAN NOT NULL,
            release_date TEXT,
            duplicate BOOLEAN NOT NULL,
            examine TEXT NOT NULL,
            icon TEXT NOT NULL,
            wiki_name TEXT,
            wiki_url TEXT,
            equpment INTEGER,
            weapon INTEGER
            )''')

db.execute('''CREATE TABLE ItemEquipment(
            id INTEGER NOT NULL PRIMARY KEY
            attack_stab INTEGER,
            attack_slash INTEGER,
            attack_crush INTEGER,
            attack_magic INTEGER,
            attack_range INTEGER,
            defence_stab INTEGER,
            defence_slash INTEGER,
            defence_crush INTEGER,
            defence_magic INTEGER,
            defence_ranged INTEGER,
            melee_strength INTEGER,
            ranged_strength INTEGER,
            magic_damage INTEGER,
            prayer INTEGER,
            slot TEXT,
            requirements TEXT
            )''')

db.execute('''ItemWeapon(
    id INTEGER NOT NULL PRIMARY KEY
    attack_speed INTEGER,
    weapon_type TEXT,
    stances TEXT
    )''')
db.execute('''Requirements(
    id INTEGER NOT NULL PRIMARY KEY,
    requirements TEXT
    )''')
    
db.close()