from flask import Flask, json, Response, request
from itertools import count, filterfalse

server = Flask(__name__)
MOVIES = {}


def _get_first_available_id():
	return next(filterfalse(set(MOVIES.keys()).__contains__, count(1)))


@server.route("/movies", methods=["GET"])
def get_movies_get_request():
	movies = [{"id": movie_id, "nume": movie["nume"]}
		for movie_id, movie in MOVIES.items()]
	return Response(response=json.dumps(movies), status=200)

@server.route("/movies", methods=["POST"])
def get_movies_post_request():
	global MOVIES
	id = _get_first_available_id()
	json_data = request.json
	if json_data and "nume" in json_data and json_data["nume"] != "":
		MOVIES[id] = json_data
		return Response(status = 201)
	return Response(status = 400) 

@server.route("/movie/<id>", methods=["GET"])
def handle_movie_id_get_request(id=None):
    global MOVIES
    movie_id = int(id)
    if movie_id not in MOVIES:
        return Response(status=404)
    movies = {"id": movie_id, "nume": MOVIES[movie_id]["nume"]}
    return Response(response=json.dumps(movies), status=200)

@server.route("/movie/<id>", methods=["PUT"])
def handle_movie_id_put_request(id=None):
    global MOVIES
    movie_id = int(id)
    if movie_id not in MOVIES:
        return Response(status=404)
    json_data = request.json
    MOVIES[movie_id] = json_data
    movies = {"id": movie_id, "nume": MOVIES[movie_id]["nume"]}
    return Response(response=json.dumps(movies), status=200)

@server.route("/movie/<id>", methods=["DELETE"])
def handle_movie_id_delete_request(id=None):
    global MOVIES
    movie_id = int(id)
    if movie_id not in MOVIES:
        return Response(status=404)
    del(MOVIES[movie_id])
    return Response(status=200)
	


@server.route("/reset", methods=["DELETE"])
def delete_all():
	global MOVIES
	MOVIES = {}

	return Response(status=200)

if __name__ == '__main__':
	server.run('0.0.0.0', debug=True)