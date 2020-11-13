from pony.orm import db_session
from datetime import datetime
import json

@db_session()
def create_items(Item):
    items = set()
    title = 'finish project',
    