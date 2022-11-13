"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "GET":
        user = User.query.all ()
        user = list(map(lambda x: x.serialize(), user))
        return jsonify(user)
        if user is not None:
            return jsonify(user.serialize())
    else:
        user = User()
        user.name = request.json.get("name")
        user.password = request.json.get("password")
        user.email = request.json.get("email")
        user.isActive = request.json.get("isActive")

        db.session.add(user)
        db.session.commit()

    return jsonify(user.serialize()), 200

@app.route("/vehicles", methods=["POST", "GET"])
def vehicles():
    if request.method == "GET":
        vehicles = Vehicles.query.all ()
        vehicles = list(map(lambda x: x.serialize(), vehicles))
        return jsonify(vehicles)
        if vehicles is not None:
            return jsonify(vehicles)
    else:
        vehicles = Vehicles()
        vehicles.name = request.json.get("name")
        vehicles.model = request.json.get("model")
        vehicles.crew = request.json.get("crew")
        vehicles.consumables = request.json.get("consumables")
        vehicles.manufacturer = request.json.get("manufacturer")

        db.session.add(vehicles)
        db.session.commit()

    return jsonify(vehicles.serialize())
@app.route("/characters", methods=["POST", "GET"])
def characters():
    if request.method == "GET":
        characters = Characters.query.all()
        characters = list(map(lambda x:x.serialize(), characters))
        return jsonify(characters)
        if characters is not None:
            return jsonify(characters)
    else:
        characters = Characters()
        characters.name = request.json.get("name")
        characters.gender = request.json.get("gender")
        characters.height = request.json.get("height")
        characters.skin_color = request.json.get("skin_color")

        db.session.add(characters)
        db.session.commit()

    return jsonify(characters.serialize())
@app.route("/planets", methods=["POST", "GET"])
def planets():
    if request.method == "GET":
        planets = Planets.query.all ()
        planets = list(map(lambda x: x.serialize(), planets))
        return jsonify(planets)
        if planets is not None:
            return jsonify(planets)
    else:
        planets = Planets()
        planets.name = request.json.get("name")
        planets.population = request.json.get("population")
        planets.terrain = request.json.get("terrain")
        planets.climate = request.json.get("climate")
        planets.gravity = request.json.get("gravity")

        db.session.add(planets)
        db.session.commit()

    return jsonify(planets.serialize())
@app.route("/favorites", methods=["POST", "GET"])
def favorites():
        if request.method == "GET":
            favorites = Favorite.query.all()
            favorites = list(map(lambda x: x.serialize(), favorites))
            return jsonify(favorites)
            if favorites is not None:
                return jsonify(favorites.serialize())   
        else:
            favorites = Favorite()
            data = request.json.get("favorite_name")
            favorites.category=request.json.get("category")
            favorites.favorite_name=request.json.get("favorite_name")
            favorites.user_id=request.json.get("user_id")
            db.session.add(favorites)
            db.session.commit()

@app.route("/favorites/<int:id>",methods=["POST","GET"])
def favorite_list(id):
    if request.method == "GET":
        if id is not None:
            favorites = Favorite.query.get(id)
            return jsonify(favorites.serialize())
        else:
            return jsonify('Missing id for route'),404  

# this only runs if `$ python src/main.py` is executed


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
