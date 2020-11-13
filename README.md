## Publicist Code Challenge

*Create a API backend for a To Do List application.*

### Goals

The goals of this challenge is to implement a RESTful API for a To Do
List application. We need to implement a "lists" resource that contains
a nested "items" resource.

You will need to do the following:

- Define new model entities in the `models.py` file.

  We are using the Pony ORM library, you can find documentation on how
  to implement model entities [here](https://docs.ponyorm.org/entities.html).
- Define new API routes in the `server.py` file.

  The new API routes should follow standard REST conventions. Full CRUD
  operations should be implemented for each resource type. Routes should
  return JSON data for the "index" and "read" operations. Routes may
  return JSON data for "create" and "update" operations.
- Implement tests for the new API routes in `test_server.py`.

  Ideally, all new routes should be fully tested with as high coverage
  as possible.

More implementation requirements are detailed below.

#### Submission

Please open a Pull Request on Github with your changes. Feel free to add
any comments or useful notes to your PR description.

### Setup

Python 3 is required to run this project and we recommend using
[Pipenv](https://pipenv.pypa.io/en/latest/).

The API server uses [web.py](https://github.com/webpy/webpy).
You can find more docs [here](https://webpy.org/cookbook/).

#### Install

First step is to install the dependencies. This can be done via Pipenv
by running:

```
pipenv install --dev
```

Alternatively, the `requirements.txt` file can also be used with `pip`:

```
pip install -r requirements.txt
```

#### Running the Server

You can run the application server with:

```
pipenv run python server.py 3005
```

Where the first command line argument is the desired port number.
Requests can be made via curl:

```
$ curl -v http://localhost:3005/
> GET / HTTP/1.1
> Host: localhost:3005
> User-Agent: curl/7.68.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json
< Transfer-Encoding: chunked
< Date: Mon, 09 Nov 2020 14:57:32 GMT
< Server: localhost
<
{"message": "ToDo List REST API", "version": "0.0.1"}
```

#### Running the Tests

Tests are run via the following command:

```
pipenv run pytest
```

### Implementation Requirements

For the purpose of this exercise, do not worry about user models or
authentication and authorization.

Here are data requirements for our API implementation:

#### API Fields

The ToDo List API implementation requires the following fields in our
`lists` resource:

- Name
- Number of completed items
- Number of total items

For the `items` resource, the following is required:

- Title
- Description
- Completed true/false flag

Feel free to add other useful fields to these, such as create and update
timestamps.

#### Tests

New tests can defined as functions in the `test_server.py` file.
`pytest` witll automatically detect and run any test function that
begins with `test_`.

A fixture is already defined which, when used as argument to a test
function, allows for test requests to be made against the API server.
For example:

```python
def test_index(test_app):
    r = test_app.get('/')

    assert r.status == 200
```

In the above function, we inject the `test_app` fixture which is used to
make test requests.  All the of the HTTP methods are available to this
test client.  Documentation is available
[here](https://web.archive.org/web/20160707041049/http://pythonpaste.org/modules/fixture.html#paste.fixture.TestApp).
