from app import db
from sqlalchemy.dialects.mysql import BIGINT


class User(db.Model):
    __tablename__ = 'users'

    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, id, name):
        self.userid = id
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.userid)

class Movie(db.Model):
    __tablename__ = 'movies'

    movieid = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.movieid)

class TagInfo(db.Model):
    __tablename__ = 'taginfo'

    tagid = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.tagid)

class Genre(db.Model):
    __tablename__ = 'genres'

    genreid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.genreid)


class Rating(db.Model):
	__tablename__ = 'ratings'
	userid = db.Column(db.Integer, db.ForeignKey('users.userid'), primary_key=True)
	movieid = db.Column(db.Integer, db.ForeignKey('movies.movieid'), primary_key=True)
	rating = db.Column(db.Integer, nullable=False)
	timestamp = db.Column(BIGINT(unsigned=True), nullable=False)

	def __repr__(self):
		return '<rating {}>'.format(self.rating)

class Tag(db.Model):
	__tablename__ = 'tags'

	userid = db.Column(db.Integer, db.ForeignKey('users.userid'), primary_key=True, nullable=False)
	movieid = db.Column(db.Integer, db.ForeignKey('movies.movieid'), primary_key=True, nullable=False)
	tagid = db.Column(db.Integer, db.ForeignKey('taginfo.tagid'), primary_key=True, nullable=False)
	timestamp = db.Column(BIGINT(unsigned=True), nullable=False)

	def __repr__(self):
		return '<userid {} : tagid {} : movieid {}>'.format(self.userid, self.tagid, self.movieid)

class HasAGenre(db.Model):
	__tablename__ = 'hasagenre'

	movieid = db.Column(db.Integer, db.ForeignKey('movies.movieid'), primary_key=True)
	genreid = db.Column(db.Integer, db.ForeignKey('genres.genreid'), primary_key=True)

	def __repr__(self):
		return '<id {}>'.format(self.id)