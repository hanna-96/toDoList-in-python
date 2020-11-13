from datetime import datetime
def def_lists_items(db, orm, List, Item):
    class ListItems(db.Entity):
        newlist = orm.Required(List, column='list_id')
        item = orm.Required(Item, column='item_id')
        custom_column = orm.Required(datetime)
    return ListItems