import json
import os
import web

# from models import List
# from models import ListInfo

# from models import Item
# from models import ItemInfo

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

class root:
    def GET(self):
        web.header('Content-Type', 'application/json')

        return json.dumps(
            dict(message="ToDo List REST API", version="0.0.1")
        )

class lists:
    def GET(self):
        pass


# class list:
#     def GET(self, id):
#         print(f'Got ID {id}')

#         pass

    # Data can be read via: web.data()
    # https://webpy.org/cookbook/postbasic
    # def POST(self):
    #    print(web.data())
    #    pass


app = web.application(urls, globals())

if os.environ.get('RUN_ENV', 'dev') != 'test' and __name__ == "__main__":
    app.run()
