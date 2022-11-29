from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters):
        sort, page = False, False
        if filters.get("status") is not None:
            sort = True
        if filters.get("page") is not None:
            page = filters.get("page")
        movies = self.dao.get_all(sort=sort, page=page)
        return movies

    #def create(self, movie_d):
        #return self.dao.create(movie_d)

    #def update(self, movie_d):
        #self.dao.update(movie_d)
        #return self.dao

    #def delete(self, rid):
        #self.dao.delete(rid)
