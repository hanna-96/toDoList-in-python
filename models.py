# from pony.orm import *
from pony  import orm
# from lists import def_users_entity
from lists import def_lists_entity
from items import def_items_entity
from create_list import creating_lists,creating_items,get_list_items,delete_list_by_id
# from lists_items import def_lists_items
# db = Database()
db = orm.Database()

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

# db_session()

# Define our model entities
# https://docs.ponyorm.org/entities.html


# class List(db.Entity):
#     # pass
#     id = PrimaryKey(int)
#     name = Required(str)
#     numberOfCompletedItems = Required(int)
#     totalItems = Required(str)
#     items = Set('Item')


# class Item(db.Entity):
#     id = PrimaryKey(int)
#     title = Required(str, unique=True)
#     description = Required(str)
#     completed = Required(bool)
#   # an entity can relate to other entities through relationship attributes
#     lists = Set(List)


# class ListInfo:
#     @db_session
#     def create(self, id,name, numberOfCompletedItems, totalItems):
#         todo = List(
#             id = id, name= name, numberOfCompletedItems=numberOfCompletedItems, totalItems=totalItems)
#         return todo

#     @db_session
#     def get_by_id(self, id):
#         return select(todo for todo in List if todo.id == id).first()


# class ItemInfo:
#     @db_session
#     def create(self, id,title, description, completed):
#         item = Item(id = id, title=title, description=description, completed=completed)
#         print(item)
#         return item

#     @db_session
#     def get_by_id(self, id):
#         return select(i for i in Item if i.id == id).first()

list_class = def_lists_entity(db,orm)
items_class = def_items_entity(db,orm,list_class)
# lists_items_class = def_lists_items(db,orm,list_class,items_class)
# get_list_items(list_class,items_class)
# Mapping entities to the database tables
db.generate_mapping(create_tables=True)
# creating_lists(list_class,items_class)
# get_list_items(list_class,items_class)
delete_list_by_id(list_class,2)