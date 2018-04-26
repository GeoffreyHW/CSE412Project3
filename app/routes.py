from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import DatabaseQueryForm
from app.models import User, Movie, Tag, Rating, TagInfo, HasAGenre, Genre
from sqlalchemy import func
from sqlalchemy.sql import label
from werkzeug.urls import url_parse

def convertGenreStringToInt(str):
	genres = {	'action' : 1,
				'adventure' : 2,
				'animation' : 3,
				'children' : 4,
				'comedy' : 5,
				'crime' : 6,
				'documentary' : 7,
				'drama' : 8,
				'fantasy' : 9,
				'film-noir' : 10,
				'horror' : 11,
				'musical' : 12,
				'mystery' : 13,
				'romance' : 14,
				'scifi' : 15,
				'thriller' : 16,
				'war' : 17,
				'western' : 18,
			}
	for key, val in genres.items():
		if str == key:
			return val
	
	return -1

@app.route('/')
@app.route('/database', methods=['GET', 'POST'])
def database():
	form = DatabaseQueryForm()

	counts = None
	avg_ratings = None
	max_count = 5
	if form.validate_on_submit():

		avg_ratings_query = db.session.query(Movie.title, Genre.genreid, func.avg(Rating.rating).label('average'))
		avg_ratings_query = avg_ratings_query.join(HasAGenre, HasAGenre.movieid==Movie.movieid)\
						.join(Genre, Genre.genreid==HasAGenre.genreid)\
						.join(Rating, Movie.movieid==Rating.movieid)

		if form.movie.data != '':
			avg_ratings_query = avg_ratings_query.filter(Movie.title.ilike('%{}%'.format(form.movie.data)))

		if form.tag.data != '':
			avg_ratings_query = avg_ratings_query.join(Tag, Movie.movieid==Tag.movieid).join(TagInfo, Tag.tagid==TagInfo.tagid).filter(TagInfo.content.ilike('%{}%'.format(form.tag.data)))		
		
		avg_ratings_query = avg_ratings_query.group_by(Movie.movieid, Genre.genreid)
		avg_ratings_query = avg_ratings_query.order_by(Movie.movieid)
		print("\nAvg Results: \n", avg_ratings_query.all())

		avg_ratings_query = avg_ratings_query.subquery('avg_ratings_query')

		filter_avg_ratings_query = db.session.query(Genre.name, func.count(Genre.name))
		filter_avg_ratings_query = filter_avg_ratings_query.filter((Genre.genreid==avg_ratings_query.c.genreid) & (avg_ratings_query.c.average >= form.min_rating.data) & (avg_ratings_query.c.average <= form.max_rating.data))

		filter_avg_ratings_query = filter_avg_ratings_query.group_by(Genre.genreid)
		filter_avg_ratings_query = filter_avg_ratings_query.order_by(Genre.name)

		counts = filter_avg_ratings_query.all()
		print("\nFiltered Count Results: \n", counts )

		genre_averages_query = db.session.query(Genre.name, func.avg(Rating.rating))
		genre_averages_query = genre_averages_query.join(HasAGenre, HasAGenre.genreid==Genre.genreid)\
						.join(Movie, Movie.movieid==HasAGenre.movieid)\
						.join(Rating, Movie.movieid==Rating.movieid)
		genre_averages_query = genre_averages_query.filter((Movie.title==avg_ratings_query.c.title) & (Genre.genreid==avg_ratings_query.c.genreid))				
		genre_averages_query = genre_averages_query.filter((Genre.genreid==avg_ratings_query.c.genreid) & (avg_ratings_query.c.average >= form.min_rating.data) & (avg_ratings_query.c.average <= form.max_rating.data))

		genre_averages_query = genre_averages_query.group_by(Genre.name)
		genre_averages_query = genre_averages_query.order_by(Genre.name)

		avg_ratings = genre_averages_query.all()
		print("\nFiltered Average Rating Results: \n", counts )

		

		# Patching up holes
		labels = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
		

		for indx, label in enumerate(labels):
			if len(avg_ratings)==indx or avg_ratings[indx][0].lower() != label.lower():
				avg_ratings.insert(indx, (label, 0.0))


		print("\nAvg Results with gaps filled in: \n", avg_ratings)


		for indx, label in enumerate(labels):
			if len(counts)==indx or counts[indx][0].lower() != label.lower():
				counts.insert(indx, (label, 0))

			max_count = max(max_count, counts[indx][1])

		print("\nCount Results with gaps filled in: \n", avg_ratings)

	return render_template('databasequery.html', form=form, avg_ratings=avg_ratings, counts=counts, max_count=max_count)