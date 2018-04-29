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

@app.route('/', methods=['GET', 'POST'])
@app.route('/database', methods=['GET', 'POST'])
def database():
	form = DatabaseQueryForm()

	counts = None
	avg_ratings = None
	max_count = 5
	if form.validate_on_submit():

		print("MIN ", request.form['min'])
		print("MAX ", request.form['max'])

		# QUERY TIME!


		# SELECT DISTINCT m.movieid, g.name, r.rating
		# FROM movies m, genres g, hasagenre h, ratings r
		# WHERE m.movieid = r.movieid AND h.movieid = m.movieid AND g.genreid = h.genreid
		# AND r.rating >= 0 AND r.rating <= 5;


		# Query to filter out by the title, tag, and rating
		filter_query = db.session.query(Movie.movieid.label('movieid'), Genre.name.label('name'), Rating.rating)
		filter_query = filter_query.join(Rating, Movie.movieid==Rating.movieid)
		filter_query = filter_query.join(HasAGenre, HasAGenre.movieid==Movie.movieid)\
		 				.join(Genre, Genre.genreid==HasAGenre.genreid)\

		# Filter movie title
		if form.movie.data != '':
			filter_query = filter_query.filter(Movie.title.ilike('%{}%'.format(form.movie.data)))

		# Filter movie tag
		if form.tag.data != '':
			filter_query = filter_query.join(Tag, Movie.movieid==Tag.movieid).join(TagInfo, Tag.tagid==TagInfo.tagid).filter(TagInfo.content.ilike('%{}%'.format(form.tag.data)))		

		# Filter rating
		filter_query = filter_query.filter((Rating.rating >= request.form['min']) & (Rating.rating <= request.form['max']))
		









		# SELECT result.name, count(result.name)
		# FROM
		# 	(SELECT DISTINCT ON (m.movieid, g.name) m.movieid, g.name, r.rating
		# 	FROM movies m, genres g, hasagenre h, ratings r
		# 	WHERE m.movieid = r.movieid AND h.movieid = m.movieid AND g.genreid = h.genreid
		# 	AND r.rating >= 0 AND r.rating <= 5) result
		# GROUP BY result.name
		# ORDER BY result.name;


		filter_query_distinct = filter_query.distinct('movieid').distinct('name')
		filter_query = filter_query.subquery('filter_query')
		filter_query_distinct = filter_query_distinct.subquery('filter_query_distinct')


		genre_counts_query = db.session.query(filter_query_distinct.c.name, func.count(filter_query_distinct.c.name))
		genre_counts_query = genre_counts_query.group_by(filter_query_distinct.c.name)
		genre_counts_query = genre_counts_query.order_by(filter_query_distinct.c.name)

		counts = genre_counts_query.all()
		print("\nFiltered Count Results: \n", counts )






		#Calculate the average ratings of every genre given the movies whose ratings are within the range of the user input

		genre_averages_query = db.session.query(filter_query.c.name, func.avg(filter_query.c.rating))
		genre_averages_query = genre_averages_query.group_by(filter_query.c.name)
		genre_averages_query = genre_averages_query.order_by(filter_query.c.name)

		avg_ratings = genre_averages_query.all()
		print("\nFiltered Average Rating Results: \n", avg_ratings )

		

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

		print("\nCount Results with gaps filled in: \n", counts)

	return render_template('databasequery.html', form=form, avg_ratings=avg_ratings, counts=counts, max_count=max_count)