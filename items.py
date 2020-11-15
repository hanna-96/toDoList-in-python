def def_items_entity(db,orm,List):
    class Item(db.Entity):
        title = orm.Required(str, unique=True)
        description = orm.Required(str)
        completed = orm.Optional(bool)
        lists = orm.Required(List,column = "list_id")
    return Item
