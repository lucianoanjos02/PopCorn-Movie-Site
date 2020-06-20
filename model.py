from sqlalchemy import Column, ForeignKey, Integer, String, Date, MetaData, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
        '''
        Classe que mapeia a tabela User na base MovieApp
        '''
        __tablename__ = 'TUser'

        id_user = Column('idUser', Integer, primary_key=True, autoincrement=True)
        login = Column('login', String(30))
        password = Column('password', String(15))
        user_name = Column('userName', String(50))
        email = Column('email', String(50))
        birth_date = ('birthDate', Date)
        favorite_movies = Column('favoriteMoviesJSON', String(5000))
        favorite_series = Column('favoriteSeriesJSON', String(5000))
        reviews = Column('reviewsJSON', String(5000))


        def __repr__ (self):
            return f'Usuario {self.name}'
    

class Movie(Base):
        '''
        Classe que mapeia a tabela Movie na base MovieApp
        '''
        __tablename__ = 'TMovie'
        __table_args__= tuple(CheckConstraint('movieRate <= 10', name='CheckMovieRate'))

        movie_id = Column('movieId', Integer, primary_key=True, autoincrement=True)
        movie_name = Column('movieName', String(100))
        movie_realese = Column('movieRealese', String(12))
        movie_runtime = Column('movieRuntime', String(10))
        movie_genre = Column('movieGenre', String(50))
        movie_director = Column('movieDirector', String(50))
        movie_writer = Column('movieWriter', String(650))
        movie_actors = Column('movieActors', String(650))
        movie_plot = Column('moviePlot', String(650))
        movie_language = Column('movieLanguage', String(100))
        movie_country = Column('movieCountry', String(100))
        movie_production = Column('movieProduction', String(100))
        movie_rate = Column('movieRate', Integer)
        movie_poster = Column('moviePoster', String(300))

        def __repr__(self):
            return f'<Movie {self.movie_name}, {self.movie_realese}, {self.movie_runtime}, {self.movie_genre}, {self.movie_director}, {self.movie_writer}, {self.movie_actors}, {self.movie_plot}, {self.movie_language}, {self.movie_country}, {self.movie_production}, {self.movie_rate},{self.movie_poster}>'

class Series(Base):
        '''
        Classe que mapeia a tabela Series na base MovieApp
        '''
        __tablename__ = 'TSeries'
        __table_args__= tuple(CheckConstraint('seriesRate <= 10', name='CheckSeriesRate'))

        series_id = Column('seriesId', Integer, primary_key=True, autoincrement=True)
        series_name = Column('seriesName', String(100))
        series_seasons = Column('seriesSeasons', Integer)
        series_realese = Column('seriesRealese', String(12))
        series_episode_runtime = Column('seriesEpisodeRuntime', String(10))
        series_genre = Column('seriesGenre', String(50))
        series_director = Column('seriesDirector', String(50))
        series_writer = Column('seriesWriter', String(650))
        series_actors = Column('seriesActors', String(650))
        series_plot = Column('seriesPlot', String(650))
        series_language = Column('seriesLanguage', String(100))
        series_country = Column('seriesCountry', String(100))
        series_rate = Column('seriesRate', Integer)
        series_poster = Column('seriesPoster', String(300))
        

        def __repr__(self):
            return f'<Series {self.series_name}, {self.series_seasons}, {self.series_realese}, {self.series_episode_runtime}, {self.series_genre}, {self.series_director}, {self.series_writer}, {self.series_actors}, {self.series_plot}, {self.series_language}, {self.series_country}, {self.series_rate}, {self.series_poster}>'