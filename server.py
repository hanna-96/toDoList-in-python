import json
import os
import web

from models import list_class, items_class
from create_list import get_all_lists, get_list, creating_lists, update_list, delete_list_by_id

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
#
# Define global classes for handling requests
##

class root:
    def GET(self):
        web.header('Content-Type', 'application/json')

        return json.dumps(
            dict(message="ToDo List REST API", version="0.0.1")
        )


class lists:
    def GET(self):
        all_lists = get_all_lists(list_class)
        return json.dumps(all_lists)


class list:
    def GET(self, id):
        print(f'Got ID {id}')
        selected_list = get_list(list_class, items_class, id)
        return json.dumps(selected_list)

    # Data can be read via: web.data()
    # https://webpy.org/cookbook/postbasic
    def POST(self, name, numberOfCompletedItems, totalItems):
        print(web.data())
        new_list = creating_lists(
            list_class, items_class, name, numberOfCompletedItems, totalItems)
        return json.dumps(new_list)

    def PUT(self, id, name):
        print(web.data())
        updated_list = update_list(list_class, id, name)
        return json.dumps(updated_list)

    def DELETE(self, id, name):
        print(web.data())
        delete_list_by_id(list_class, id)


app = web.application(urls, globals())

if os.environ.get('RUN_ENV', 'dev') != 'test' and __name__ == "__main__":
    app.run()
