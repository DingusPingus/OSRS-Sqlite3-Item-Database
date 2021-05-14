import sqlite3
from osrsbox import items_api
def insert():
    items = items_api.load()

    db = sqlite3.connect('OSRSItems.db')
    c = db.cursor()
    print('inserting osrs items...')
    for item in items:
        #item properties insertion
        c.execute('''INSERT INTO ItemProperties(id, name, last_updated, incomplete, members, tradeable, tradeable_on_ge, 
                                            stackable, stacked, noted, noteable, linked_id_item, linked_id_noted, linked_id_placeholder,
                                            placeholder, equipable_by_player, equipable_weapon, cost, lowalch, highalch, weight, buy_limit,
                                            quest_item, release_date, duplicate, examine, icon, wiki_name, wiki_url, equipment, weapon)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                    (item.id, item.name, item.last_updated, item.incomplete, item.members, item.tradeable, item.tradeable_on_ge, item.stackable, 
                    item.stacked, item.noted, item.noteable, item.linked_id_item, item.linked_id_noted, item.linked_id_placeholder, item.placeholder,
                    item.equipable_by_player, item.equipable_weapon, item.cost, item.lowalch, item.highalch, item.weight, item.buy_limit, item.quest_item,
                    item.release_date, item.duplicate, item.examine, item.icon, item.wiki_name, item.wiki_url, item.equipment, item.weapon))
        #equipable item insertion
        # if(item.equipable_by_player):
        #     c.execute('''INSERT INTO ItemEquipment(id, attack_stab, attack_slash, attack_crush, attack_magic, attack_range, defence_stab,
        #                                             defence_slash, defence_crush, defence_magic, defence_ranged, melee_strength, ranged_strength,
        #                                             magic_damage, prayer, slot)
        #                 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
        #                 (item.id, item.equipment['attack_stab'], item.equipment['attack_slash'], item.equipment['attack_crush'], item.equipment['attack_magic'],
        #                 item.equipment['attack_range'], item.equipment['attack_stab'], item.equipment['defence_slash'], item.equipment['defence_crush'], item.equipment['defence_magic'],
        #                 item.equipment['defence_ranged'], item.equipment['melee_strength'], item.equipment['ranged_strength'], item.equipment['magic_damage'], item.equipment['prayer'],
        #                 item.equipment['slot']))
            
        #     c.execute('''INSERT INTO Requirements(id, requirements)
        #                 VALUES(?,?)''',())
        #     if(item.equipable_weapon):
        #         c.execute('''INSERT INTO Item Weapon()''')
    db.commit()
    db.close()