import datetime

from pony.orm import *
from database import db


class Reporter(db.Entity):
    id = PrimaryKey(int, auto=False)
    first_name = Required(str)
    last_name = Optional(str)
    username = Optional(str)
    reported = Set("Believer")
    created = Required(datetime.datetime, default=datetime.datetime.now)

    def __str__(self):
        s = self.first_name
        if self.last_name:
            s += " " + self.last_name

        if self.username:
            s += " (@%s)" % self.username

        return s

    def __repr__(self):
        return str(self)
