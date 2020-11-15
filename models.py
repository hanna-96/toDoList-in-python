# from pony.orm import *
from pony  import orm
from pony.orm import db_session


from lists import def_lists_entity
from items import def_items_entity
from create_list import creating_lists,creating_items,get_list_items,delete_list_by_id,update_list,get_all_lists,get_list

db = orm.Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

# Define our model entities
# https://docs.ponyorm.org/entities.html

list_class = def_lists_entity(db,orm)
items_class = def_items_entity(db,orm,list_class)

# Mapping entities to the database tables
db.generate_mapping(create_tables=True)
# creating_lists(list_class,items_class,'solve_algo',2)
# creating_lists(list_class,items_class,'project',1,3)
# creating_lists(list_class,items_class,'Christmas_preperation',1,1)

# get_list_items(list_class,items_class)
# delete_list_by_id(list_class,1)
update_list(list_class,2,'solve_algo',5,10)
# get_list(list_class,1)
# get_by_id(list_class,1)
# get_all_lists(list_class)
# get_items_from_list(items_class,list_class)
# get_list(list_class,items_class,1)