"""
Backend Routes for Races

Kyle Infantino 6/13/19
"""
import json
from flask import Flask, request
from db import db, Race
from datetime import datetime



app = Flask(__name__)

db_filename = 'races.db'

# SELECT * FROM RACE WHERE
# print(races)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

#test
@app.route('/api/')
def test():
    return "Welcome to the Race Finder!"

#Get all Races
@app.route('/api/allraces/')
def getAllRaces():
    races = Race.query.order_by(Race.dateStart).all()
    get = {'success': True, 'data': [race.serialize() for race in races]}
    return json.dumps(get), 200

@app.route('/api/allinorder/')
def getInOrder():
    races = Race.query.all()
    get = {'success': True, 'data': [race.serialize() for race in races]}
    return json.dumps(get), 200

#Add a Race
@app.route('/api/addrace/', methods=['POST'])
def addRace():
    body = json.loads(request.data)
    race = Race(
        name= body.get('name'),
        dateStart = body.get('dateStart'),
        dateEnd = body.get('dateEnd'),
        location = body.get('location'),
        website = body.get('website'),
        fiveK = body.get('fiveK'),
        tenK = body.get('tenK'),
        halfMarathon = body.get('halfMarathon'),
        marathon = body.get('marathon'),
        challenges = body.get('challenges'),
        otherDistance = body.get('otherDistance'),
        lat = body.get('lat'),
        long = body.get('long'),
    )
    db.session.add(race)
    db.session.commit()
    return json.dumps({'success': True, 'data': race.serialize()}), 201


#Edit a Race - set validated field to False
@app.route('/api/editrace/<string:racename>/', methods = ['POST'])
def editRace(racename):
    race = Race.query.filter_by(name = racename).first()
    if race is not None:
        body = json.loads(request.data)
        race.name= body.get('name')
        race.dateStart = datetime.strptime(body.get('dateStart'), '%m/%d/%y')
        race.dateEnd = datetime.strptime(body.get('dateEnd'), '%m/%d/%y')
        race.location = body.get('location')
        race.website = body.get('website')
        race.fiveK = body.get('fiveK')
        race.tenk = body.get('tenK')
        race.halfMarathon = body.get('halfMarathon')
        race.marathon = body.get('marathon')
        race.challenges = body.get('challenges')
        race.otherDistance = body.get('otherDistance')
        race.lat = body.get('lat')
        race.long = body.get('long')
        db.session.commit()
        return json.dumps({'success': True, 'data': race.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Race not found!'}), 404

@app.route('/api/editcoord/<string:racename>/', methods = ['POST'])
def editRaceCoord(racename):
    race = Race.query.filter_by(name = racename).first()
    if race is not None:
        body = json.loads(request.data)
        race.lat = body.get('lat')
        race.long = body.get('long')
        db.session.commit()
        return json.dumps({'success': True, 'data': race.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Race not found!'}), 404

@app.route('/api/specificRace/<string:racename>/')
def getSpecific(racename):
    race = Race.query.filter_by(name = racename).first()
    if race is not None:
        return json.dumps({'success': True, 'data': race.serialize()}), 200
    else:
        return json.dumps({'success': False, 'error': 'Race not found!'}), 404


@app.route('/api/deleteRace/<string:racename>/snook/', methods = ['Delete'])
def deleterace(racename):
    race = Race.query.filter_by(name = racename).first()
    if race is not None:
        db.session.delete(race)
        db.session.commit()
        return json.dumps({'success': True, 'data': race.serialize()}), 200
    else:
        return json.dumps({'success': False, 'error': 'Race not found!'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
