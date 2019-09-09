"""
Backend db file for Races

Kyle Infantino 6/13/19
"""



# add approved field for when race validated by me
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Race(db.Model):
    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dateStart = db.Column(db.DateTime(), nullable = False)
    dateEnd = db.Column(db.DateTime(), nullable = False)
    location = db.Column(db.String, nullable = False)
    website = db.Column(db.String, nullable = False)
    fiveK = db.Column(db.Boolean, nullable = False)
    tenK = db.Column(db.Boolean, nullable = False)
    halfMarathon = db.Column(db.Boolean, nullable = False)
    marathon = db.Column(db.Boolean, nullable = False)
    challenges = db.Column(db.String, nullable = False)
    otherDistance = db.Column(db.String, nullable = False)
    lat = db.Column(db.Float, nullable = False)
    long = db.Column(db.Float, nullable = False)

    def __init__(self, **kwargs):
        assert kwargs.get('name') != ""
        assert kwargs.get('dateStart') != ""
        assert kwargs.get('dateEnd') != ""
        assert kwargs.get('location') != ""
        assert type(kwargs.get('lat')) == float 
        assert type(kwargs.get('long')) == float

        self.name = kwargs.get('name')
        self.dateStart = datetime.strptime(kwargs.get('dateStart'), '%m/%d/%y')
        self.dateEnd = datetime.strptime(kwargs.get('dateEnd'), '%m/%d/%y')
        self.location = kwargs.get('location')
        self.website = kwargs.get('website')
        self.fiveK = kwargs.get('fiveK')
        self.tenK = kwargs.get('tenK')
        self.halfMarathon = kwargs.get('halfMarathon')
        self.marathon = kwargs.get('marathon')
        self.challenges = kwargs.get('challenges')
        self.otherDistance = kwargs.get('otherDistance')
        self.lat = kwargs.get('lat')
        self.long = kwargs.get('long')

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'dateStart': self.dateStart.strftime("%m/%d/%y"),
            'dateEnd': self.dateEnd.strftime("%m/%d/%y"),
            'location': self.location,
            'website': self.website,
            'fiveK': self.fiveK,
            'tenK': self.tenK,
            'halfMarathon': self.halfMarathon,
            'marathon': self.marathon,
            'challenges': self.challenges,
            'otherDistance': self.otherDistance,
            'lat': self.lat,
            'long': self.long
        }
