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
# @db_session()
# def creating_lists(List):
#     lists = set()
#     all_lists = list(lists)
#     for l in all_lists:List(type=l)
        # List(
        #     name='MondayToDo',
        #     numberOfCompletedItems=0,
        #     totalItems=2,
        #     )
        # List(
        #     name='beforeBirthday',
        #     numberOfCompletedItems=1,
        #     totalItems=1,
        #     )
        # List(
        #     name='party',
        #     numberOfCompletedItems=1,
        #     totalItems=1,
        #     )
        # creating_items(List, Item)


@db_session()
def creating_items(List, Item):
    lists = List.select()
    for l in lists:
        Item(title=fake.name(), description=fake.name(), completed='true', lists=l)
        # Item(title='sleep', description='have some rest', completed='false',lists = l)


# get  todo lists for each item
@db_session()
def get_list_items(List,Item):
    print(
        json.dumps({'data':[i.lists.to_dict() for i in Item.select()]})
    )
# to_dict() will give us a todo for each item