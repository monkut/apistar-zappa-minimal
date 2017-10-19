import datetime
import warnings
import json
import arrow
from apistar import Route, http, Response
from apistar.frameworks.wsgi import WSGIApp as App


def healthcheck() -> Response:
    return Response({'message': '200 healthy!'}, status=200)


def index() -> Response:
    return Response({'message': '200 installed!'}, status=200)


routes = [
    Route('/healthcheck', 'GET', healthcheck),
    Route('/', 'GET', index),
]

app = App(routes=routes)
