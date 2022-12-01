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
