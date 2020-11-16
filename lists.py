def def_lists_entity(db,orm):
    class List(db.Entity):
        name = orm.Required(str)    
        totalItems = orm.Required(int)
        numberOfCompletedItems = orm.Optional(int)
        items = orm.Set('Item')
    return List
