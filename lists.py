def def_lists_entity(db,orm):
    class List(db.Entity):
        name = orm.Required(str)    
        numberOfCompletedItems = orm.Optional(int)
        totalItems = orm.Required(int)
        items = orm.Set('Item')
    return List
