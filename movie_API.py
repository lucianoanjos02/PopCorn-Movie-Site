import config
import requests
from model import Movie, Series
from dao import MovieDAO, SeriesDAO
import db_connection
from flask import Flask, jsonify


api = Flask(__name__)

# ---------- Objetos de conexão com o banco ----------
movie_dao = MovieDAO(db_connection.session)
series_dao = SeriesDAO(db_connection.session)

# ---------- URLs da API da OMDB para SÉRIES e FILMES ----------
movie_OMDBapi = 'http://www.omdbapi.com/?apikey=82500bf4&type=movie&t='
series_OMDBapi = 'http://www.omdbapi.com/?apikey=82500bf4&type=series&t='


@api.route('/')
def main():
    '''
    - Rota "raíz" da API.
    - Retorna apenas um JSON com as informações:
        - "page" : "main page"
        - "content" : None
    '''
    return jsonify({"page": "main page", "content": None})

@api.route('/movie/<movie_name>')
def get_movie(movie_name):
    '''
    - URL da rota: http://localhost:5000/movie/<movie_name>

    - Rota que faz uma requisição GET na URL movie_OMDBapi, para retornar o JSON
    com as informações do filme especificado pelo nome (movie_name). 
    
    - Caso o filme já esteja cadastrada no banco, os dados do JSON são montados 
    à partir das informações da tabela TMovie.

    - Caso o filme NÃO esteja cadastrada no banco, os dados do JSON são montados à 
    partir do JSON da API movie_OMDBapi.

    Os dados contidos no JSON/TMovie são:

    - 'Title': nome/titulo do filme.
    - 'Released': data de estreia do filme.
    - 'Runtime': tempo de duração do filme.
    - 'Genre': genêro(s) do filme.
    - 'Director': diretor do filme.
    - 'Writer': escritor(a) do filme.
    - 'Actors': atores/atrizes do filme.
    - 'Plot': trama/enrredo do filme.
    - 'Language': idiomas do filme.
    - 'Country': país/paises do filme.
    - 'Production': produtora do filme.
    - 'Poster': URL do poster do filme.
    '''
    request = requests.get(f'{movie_OMDBapi}{movie_name}')
    request_json = request.json()
    if "Error" in request_json:
        return jsonify(request_json)
    movie = movie_dao.get_movie_name(movie_name)
    if movie == None:
        new_movie = Movie(movie_name=request_json['Title'], 
                        movie_realese=request_json['Released'],
                        movie_runtime=request_json['Runtime'],
                        movie_genre=request_json['Genre'],
                        movie_director=request_json['Director'],
                        movie_writer=request_json['Writer'],
                        movie_actors=request_json['Actors'],
                        movie_plot=request_json['Plot'],
                        movie_language=request_json['Language'],
                        movie_country=request_json['Country'],
                        movie_production=request_json['Production'],
                        movie_poster=request_json['Poster'])
        save_movie = movie_dao.register_movie(new_movie)
        movie = {
                    "Title": request_json['Title'],
                    "Released": request_json['Released'],
                    "Runtime": request_json['Runtime'],
                    "Genre": request_json['Genre'],
                    "Director": request_json['Director'],
                    "Writer": request_json['Writer'],
                    "Actors": request_json['Actors'],
                    "Plot": request_json['Plot'],
                    "Language": request_json['Language'],
                    "Country": request_json['Country'],
                    "Production": request_json['Production'],
                    "Poster": request_json['Poster']
                }
        return jsonify(movie)
    else:
        movie = movie_dao.get_movie_data(movie_name)
        for movie_data in movie:
            movie = {
                    "Title": movie_data.movie_name,
                    "Released": movie_data.movie_realese,
                    "Runtime": movie_data.movie_runtime,
                    "Genre": movie_data.movie_genre,
                    "Director": movie_data.movie_director,
                    "Writer": movie_data.movie_writer,
                    "Actors": movie_data.movie_actors,
                    "Plot": movie_data.movie_plot,
                    "Language": movie_data.movie_language,
                    "Country": movie_data.movie_country,
                    "Production": movie_data.movie_production,
                    "Poster": movie_data.movie_poster
                }
        return jsonify(movie)


@api.route('/series/<series_name>')
def get_serie(series_name):
    '''
    - URL da rota: http://localhost:5000/series/<series_name>

    - Rota que faz uma requisição GET na URL series_OMDBapi, para retornar o JSON
    com as informações da série especificada pelo nome (series_name). 
    
    - Caso a série já esteja cadastrada no banco, os dados do JSON são montados 
    à partir das informações da tabela TSeries.

    - Caso a série não esteja cadastrada no banco, os dados do JSON são montados à 
    partir do JSON da API series_OMDBapi.

    Os dados contidos no JSON/TSeries são:

    - 'Title': nome/titulo da série.
    - 'Released': data de estreia do episódio piloto da série.
    - 'Seasons': quantidade de temporadas.
    - 'Runtime': tempo de cada episódio.
    - 'Genre': genêro(s) da série.
    - 'Director': diretor da série (geralmente sendo N/A).
    - 'Writer': escritor(a) da série.
    - 'Actors': atores/atrizes da série.
    - 'Plot': trama/enrredo da série.
    - 'Language': idiomas da série.
    - 'Country': país/paises da série.
    - 'Poster': URL do poster da série.
    '''
    request = requests.get(f'{series_OMDBapi}{series_name}')
    request_json = request.json()
    if "Error" in request_json:
        return jsonify(request_json)
    series = series_dao.get_series_name(series_name)
    if series == None:
        new_series = Series(series_name=request_json['Title'], 
                            series_realese=request_json['Released'],
                            series_seasons=request_json['totalSeasons'],
                            series_episode_runtime=request_json['Runtime'],
                            series_genre=request_json['Genre'],
                            series_director=request_json['Director'],
                            series_writer=request_json['Writer'],
                            series_actors=request_json['Actors'],
                            series_plot=request_json['Plot'],
                            series_language=request_json['Language'],
                            series_country=request_json['Country'],
                            series_poster=request_json['Poster'])
        save_series = series_dao.register_series(new_series)
        series = {
                    "Title": request_json['Title'],
                    "Released": request_json['Released'],
                    "Seasons": request_json['totalSeasons'],
                    "Runtime": request_json['Runtime'],
                    "Genre": request_json['Genre'],
                    "Director": request_json['Director'],
                    "Writer": request_json['Writer'],
                    "Actors": request_json['Actors'],
                    "Plot": request_json['Plot'],
                    "Language": request_json['Language'],
                    "Country": request_json['Country'],
                    "Poster": request_json['Poster']
                }
        return jsonify(series)
    else:
        series = series_dao.get_series_data(series_name)
        for series_data in series:
            series = {
                    "Title": series_data.series_name,
                    "Released": series_data.series_realese,
                    "Seasons": series_data.series_seasons,
                    "Runtime": series_data.series_episode_runtime,
                    "Genre": series_data.series_genre,
                    "Director": series_data.series_director,
                    "Writer": series_data.series_writer,
                    "Actors": series_data.series_actors,
                    "Plot": series_data.series_plot,
                    "Language": series_data.series_language,
                    "Country": series_data.series_country,
                    "Poster": series_data.series_poster
                }
        return jsonify(series)


if __name__ == '__main__':
    api.run(host=config.API_HOST, port=config.API_PORT, debug=config.API_DEBUG)