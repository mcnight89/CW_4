from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self, sort=False, page=False):
        if page and sort:
            movies = self.session.query(Movie).order_by(Movie.year.desc()).paginate(page=int(page), per_page=12).items
        elif sort:
            movies = self.session.query(Movie).order_by(Movie.year.desc()).all()
        elif page:
            movies = self.session.query(Movie).paginate(page=int(page), per_page=12).items
        else:
            movies = self.session.query(Movie).all()
        return movies

    # def get_by_director_id(self, val):
    # return self.session.query(Movie).filter(Movie.director_id == val).all()

    # def get_by_genre_id(self, val):
    # return self.session.query(Movie).filter(Movie.genre_id == val).all()

    # def get_by_year(self, val):
    # return self.session.query(Movie).filter(Movie.year == val).all()

    # def create(self, movie_d):
    # ent = Movie(**movie_d)
    # self.session.add(ent)
    # self.session.commit()
    # return ent

    # def delete(self, rid):
    # movie = self.get_one(rid)
    # self.session.delete(movie)
    # self.session.commit()

    # def update(self, movie_d):
    # movie = self.get_one(movie_d.get("id"))
    # movie.title = movie_d.get("title")
    # movie.description = movie_d.get("description")
    # movie.trailer = movie_d.get("trailer")
    # movie.year = movie_d.get("year")
    # movie.rating = movie_d.get("rating")
    # movie.genre_id = movie_d.get("genre_id")
    # movie.director_id = movie_d.get("director_id")

    # self.session.add(movie)
    # self.session.commit()
