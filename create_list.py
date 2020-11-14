from pony.orm import db_session
import json

from faker import Faker
fake = Faker()

# creating lists
@db_session()
def creating_lists(List, Item, amount=10):
    for _ in range(amount):
        List(
            name=fake.name(),
            numberOfCompletedItems=fake.random_int(0, 10),
            totalItems=fake.random_int(0, 20),
        )
        # List(
        #     name='party',
        #     numberOfCompletedItems=1,
        #     totalItems=1,
        #     )
        creating_items(List, Item)

@db_session()
def creating_items(List, Item):
    lists = List.select()
    for l in lists:
        Item(title=fake.name(), description=fake.name(), completed='true', lists=l)
        # Item(title='sleep', description='have some rest', completed='false',lists = l)


@db_session()
def get_list(List,id):
    # specific_list = List.select(lambda specific_list: specific_list.id == id)
    # selected_list = List[id]
    # all_lists = List.select()
   print(json.dumps({'data': [[l.to_dict()] for l in List.select(lambda l: l.id == id)]})) 


@db_session
def get_all_lists(List):
    print(
        json.dumps({'data': [[l.to_dict()] for l in List.select()]})
    )


# get  todo lists for each item
@db_session()
def get_list_items(List, Item):
    print(
        json.dumps({'data': [i.lists.to_dict() for i in Item.select()]})
    )
# to_dict() will give us a todo for each item



@db_session
def update_list(List, id,name):
    List[id].name = name


@db_session
def delete_list_by_id(List, id):
    specific_list = List.select(lambda specific_list: specific_list.id == id)
    specific_list.delete()

