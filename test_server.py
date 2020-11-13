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
