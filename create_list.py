from pony.orm import db_session
import json

from faker import Faker
fake = Faker()

# creating lists
@db_session()
def creating_lists(List, Item, name, totalItems,numberOfCompletedItems = '0' ):
    List(
        name=name,
        numberOfCompletedItems=numberOfCompletedItems,
        totalItems=totalItems,
        )
    creating_items(List, Item)

@db_session()
def creating_items(List, Item,completed = False):
    lists = List.select()
    for l in lists:
        if len(l.items) == 0:
            for _ in range(l.totalItems):
                Item(title=fake.name(), description=fake.name(),completed = completed, lists=l)
            

@db_session
def get_all_lists(List):
    print(
        json.dumps({'data': [[l.to_dict()] for l in List.select()]})
    )


@db_session()
def get_list(List, Item, id):
        print(json.dumps({'todo_list': [[l.to_dict()] for l in List.select(lambda l: l.id == id)]}),
        json.dumps({'items': [i.to_dict() for i in List[id].items]})),
# to_dict() will give us a todo for each item


# get  todo lists for each item
@db_session()
def get_list_items(List, Item):
    print(
        json.dumps({'data': [i.lists.to_dict() for i in Item.select()]})
    )

@db_session
def update_list(List, id, name,numberOfCompletedItems,totalItems):
    List[id].name = name
    List[id].numberOfCompletedItems = numberOfCompletedItems
    List[id].totalItems = totalItems




@db_session
def delete_list_by_id(List, id):
    specific_list = List.select(lambda specific_list: specific_list.id == id)
    specific_list.delete()

