import db_connection
from model import Movie, Series, User

class UserDAO:
    def __init__(self, data_base):
        self.__data_base = data_base
    
    def get_user(self, login):
        user = self.__data_base.query(User).filter(User.login == login).first()
        return user
    
    def register_user(self, user):
        try:
            self.__data_base.add(user)
            self.__data_base.commit()
        except:
            print("Erro ao cadastrar usuário")
            self.__data_base.rollback()
        finally:
            self.__data_base.close()
        return 'Usuário cadastrado com sucesso'
        


class MovieDAO:
    '''
    Classe que realiza a conexão entre a API e o banco, realizando transções
    na tabela TMovie.
    '''
    def __init__(self, data_base):
        '''
        Construtor recebe à sessão de conexão com o banco.
        '''
        self.__data_base = data_base
    
    def register_movie(self, movie):
        '''
        Insere um Filme na tabela TMovie
        '''
        try:
            self.__data_base.add(movie)
            self.__data_base.commit()
        except:
            print("Erro ao inserir filme")
            self.__data_base.rollback()
        finally:
            self.__data_base.close()
        return 'Filme inserido no banco'
    
    def get_movie_name(self, movie_name):
        '''
        Busca o nome de um Filme na tabela TMovie, à partir do nome
        passado como parâmetro (movie_name).
        '''
        movie = self.__data_base.query(Movie.movie_name).filter(Movie.movie_name == movie_name).first()
        return movie

    def get_movie_data(self, movie_name):
        '''
        Busca os dados de um Filme na tabela TMovie, à partir do nome
        passado como parâmetro (movie_name).
        '''
        movie = self.__data_base.query(Movie).filter(Movie.movie_name == movie_name).all() 
        return movie


class SeriesDAO:
    '''
    Classe que realiza a conexão entre a API e o banco, realizando transções
    na tabela TSeries.
    '''
    def __init__(self, data_base):
        '''
        Construtor recebe à sessão de conexão com o banco.
        '''
        self.__data_base = data_base
    
    def register_series(self, series):
        '''
        Insere uma Série na tabela TSeries
        '''
        try:
            self.__data_base.add(series)
            self.__data_base.commit()
        except:
            print("Erro ao inserir série")
            self.__data_base.rollback()
        finally:
            self.__data_base.close()
        return 'Serie inserida no banco'
    
    def get_series_name(self, series_name):
        '''
        Busca o nome de uma Série na tabela TSeries, à partir do nome
        passado como parâmetro (series_name).
        '''
        series = self.__data_base.query(Series.series_name).filter(Series.series_name == series_name).first() 
        return series

    def get_series_data(self, series_name):
        '''
        Busca os dados de uma Série na tabela TSeries, à partir do nome
        passado como parâmetro (series_name).
        '''
        series = self.__data_base.query(Series).filter(Series.series_name == series_name).all() 
        return series
