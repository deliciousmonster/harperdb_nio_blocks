from nio.block.base import Block
from nio.properties import (VersionProperty, StringProperty, IntProperty, BoolProperty, ObjectProperty, PropertyHolder)
from nio.util.discovery import not_discoverable
import base64
import requests
import json

class DatabaseConnection(PropertyHolder):
    server = StringProperty(title='Server', default='localhost', order=0)
    port = IntProperty(title='Port', default=9925, order=1)
    ssl = BoolProperty(title='Use SSL', default=False, order=2)
    allow_redirects = BoolProperty(title='Allow Redirects', default=False, order=3)
    timeout = IntProperty(title='Timeout', default=15, order=4)

class DatabaseCredentials(PropertyHolder):
    userid = StringProperty(title='User ID', default='HDB_ADMIN', allow_none=True, order=5)
    password = StringProperty(title="Password", default='password', allow_none=True, order=6)

@not_discoverable
class HarperDBBase(Block):
    version = VersionProperty('0.1.0')
    dbserver = ObjectProperty(DatabaseConnection, title='Database Connection', order=0)
    dbcreds = ObjectProperty(DatabaseCredentials, title='Database Credentials', order=1)

    def __init__(self):
        super().__init__()

    def configure(self, context):
        super().configure(context)
        protocol = "https" if self.dbserver().ssl() else "http"
        self.url = "{}://{}:{}".format(protocol, self.dbserver().server(), self.dbserver().port())
        self.headers = {
          "Content-Type": "application/json",
          "Authorization": "Basic {}".format(base64.b64encode(bytes('{}:{}'.format(self.dbcreds().userid(), self.dbcreds().password()), 'utf-8')).decode("ascii"))
        }

    def sendQuery(self, payload):
        result = requests.post(self.url, headers = self.headers, json=payload, allow_redirects=self.dbserver().allow_redirects(), timeout=self.dbserver().timeout())
        return json.loads(result.text)

