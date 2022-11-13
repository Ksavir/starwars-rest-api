from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    isActive = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User %r>" % self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'isActive': self.isActive,
        }

    def serialize_just_username(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    model=db.Column(db.String(250))
    crew=db.Column(db.Integer)
    manufacturer=db.Column(db.String(250))
    consumables=db.Column(db.Integer)
    favorite = db.relationship("Favorite",lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<Vehicles %r>" % self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'crew': self.crew,
            'consumables': self.consumables,
            'manufacturer': self.manufacturer

        }
    def serializa_just_name_manufacturer(self):
        return{
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250))
    height = db.Column(db.Integer)
    skin_color = db.Column(db.String(250))
    favorite = db.relationship('Favorite',lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<Characters %r>" % self.id

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'height': self.height,
            'skin_color': self.skin_color
        }
    def serializa_just_name_gender(self):
        return{
            'id': self.id,
            'gender': self.gender,
            'name': self.name
        }


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    gravity = db.Column(db.String(250))
    favorite = db.relationship("Favorite",lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<Planets %r>" % self.id

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'population': self.population,
            'climate': self.climate,
            'terrain':self.terrain,
            'gravity': self.gravity
        }

    def serialize_name_terrain(self):
        return{
            'id': self.id,
            'name': self.name,
            'terrain': self.terrain
        }

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30))
    favorite_name = db.Column(db.String(50))
    user = db.relationship("User",backref=db.backref('user',lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return "<Favorite %r>" % self.id

    def serialize(self):
        return{
            'id':self.id,
            'category':self.category,
            'favorite_name':self.favorite_name,
            'user_id':self.user_id
        }

    def serialize_just_user_fav(self):
        return{
        'id': self.id,
        'category': self.category,
        'favorite_name':self.favorite_name
        }