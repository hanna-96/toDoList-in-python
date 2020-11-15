import json

from pytest import fixture # added
from paste.fixture import TestApp

from server import app


@fixture
def test_app():
    middleware = []

    return TestApp(app.wsgifunc(*middleware))


def test_index(test_app):
    r = test_app.get('/')

    assert r.status == 200

    json_body = json.loads(r.body)

    assert json_body['message'] == 'ToDo List REST API'
    assert json_body['version'] == '0.0.1'

def test_index1(test_app):
    r = test_app.get('/lists')

    assert r.status == 200

    # json_body = json.loads(r.body)

    # assert json_body['message'] == 'ToDo List REST API'
    # assert json_body['version'] == '0.0.1'



# def test_myapp(test_app):
#     res = test_app.get('/lists', params={'id': 1})
#     res.mustcontain('Item 1')
#     # res = app.post('/lists', params={'id': 1, 'name': 'New item name'})
#     # The app does POST-and-redirect...
#     res = res.follow()
#     assert res.request.url == '/lists?id=1'
#     res.mustcontain('New item name')
#     res.mustcontain('Item updated')

