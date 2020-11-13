def def_items_entity(db,orm,List):
    class Item(db.Entity):
        # id = orm.PrimaryKey(int)
        title = orm.Required(str, unique=True)
        description = orm.Required(str)
        completed = orm.Required(bool)
        lists = orm.Required(List,column = "list_id")
        # item belong to list
        # lists_items = orm.Set('ListItems')

    return Item
