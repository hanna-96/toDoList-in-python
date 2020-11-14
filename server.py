import json
import os
import web

from models import list_class
# from pony  import orm
# from pony.orm import db_session
# db = orm.Database()

# db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


# from lists import def_lists_entity
# from items import def_items_entity
from create_list import get_all_lists,get_list

##
# Define our routes:
# https://webpy.org/cookbook/url_handling
##
urls = (
    '/', 'root',
    '/lists', 'lists',

    # URLs support parameter matching
    # https://webpy.org/cookbook/url_handling#capture-parameters
    '/lists/(.+)', 'list'
)


# testing for myself
# urls = ("/.*", "hello")

# class hello:
#     def GET(self):
#         return 'Hello, world!'

#
# Define global classes for handling requests
##

# list_class = def_lists_entity(db,orm)
class root:
    def GET(self):
        web.header('Content-Type', 'application/json')

        return json.dumps(
            dict(message="ToDo List REST API", version="0.0.1")
        )

class lists:
    def GET(self):
        # pass
        all_lists = get_all_lists(list_class)
        # all_lists = db.select('List')
        # return render.index(all_lists)
        return json.dumps(
            all_lists
        )

class list:
    def GET(self, id):
        print(f'Got ID {id}')
        selected_list = get_list(list_class,id)
        return json.dumps(selected_list)

    # Data can be read via: web.data()
    # https://webpy.org/cookbook/postbasic
    # def POST(self):
    #    print(web.data())
    #    pass




app = web.application(urls, globals())

if os.environ.get('RUN_ENV', 'dev') != 'test' and __name__ == "__main__":
    app.run()
