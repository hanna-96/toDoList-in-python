def def_lists_entity(db,orm):
    class List(db.Entity):
        name = orm.Required(str)    
        numberOfCompletedItems = orm.Required(int)
        totalItems = orm.Required(int)
        items = orm.Set('Item')
        # list has many items
        # lists_items = orm.Set('ListItems')
    return List
