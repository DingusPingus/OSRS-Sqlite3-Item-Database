import sqlite3
from osrsbox import items_api
def insert():
    items = items_api.load()

    db = sqlite3.connect('OSRSItems.db')
    c = db.cursor()
    print('inserting osrs items...')
    for item in items:

        c.execute('''INSERT INTO ItemProperties(id, name, last_updated, incomplete, members, tradeable, tradeable_on_ge, 
                                            stackable, stacked, noted, noteable, linked_id_item, linked_id_noted, linked_id_placeholder,
                                            placeholder, equipable_by_player, equipable_weapon, cost, lowalch, highalch, weight, buy_limit,
                                            quest_item, release_date, duplicate, examine, icon, wiki_name, wiki_url)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                    (item.id, item.name, item.last_updated, item.incomplete, item.members, item.tradeable, item.tradeable_on_ge, item.stackable, 
                    item.stacked, item.noted, item.noteable, item.linked_id_item, item.linked_id_noted, item.linked_id_placeholder, item.placeholder,
                    item.equipable_by_player, item.equipable_weapon, item.cost, item.lowalch, item.highalch, item.weight, item.buy_limit, item.quest_item,
                    item.release_date, item.duplicate, item.examine, item.icon, item.wiki_name, item.wiki_url))
    db.commit()
    db.close()