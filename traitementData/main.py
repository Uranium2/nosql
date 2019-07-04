from pymongo import MongoClient
from utils import *
from cleanIMBD import *
import json
from imdb import IMDb
import xmljson
from xml.etree.ElementTree import fromstring
from config import *
from py2neo import Graph

if __name__ == "__main__":

    # Connexion mongoDB
    database = MongoClient(mongoServer).myMovies
    print(database)

    # Connection Neo4J
    graph = Graph(uriNeo, password=passwordNeo)
    graph.schema.create_uniqueness_constraint('Movie', 'Person')

    # Create BIG JSON
    ret = {"allMovies":[]}

    # Connection API
    ia = IMDb()
    base = None

    # Foreach movie id
    for i in range(idMin, idMax):
        try:
            print(i)
            film = ia.get_movie(i)
            film = film.asXML()

            xml = fromstring(film)

            tmpJSON = xmljson.badgerfish.data(xml)
            tmpSTR = json.dumps(tmpJSON).replace("$", "do_")
            tmpJSON = json.loads(tmpSTR)

            ret["allMovies"].append(tmpJSON)
            # insert(collection1, tmpJSON)

        except:
            print("erreur", i)

    # Save file
    with open('films_big.json', "w") as f:
        print(json.dumps(ret), file=f)

    cleanDico = createCleanDictionary(ret)

    # Save clean JSON
    with open("outputs.json", "w") as out:
        json.dump(cleanDico, out)


    for movie in cleanDico["allMovies"]:

        # Insert movie information in mongoDB
        insertMovieInformation(database, movie)

        # Insert person information in mongoDB
        insertPersonInformation(database, movie)

        # insertMovie
        graph.run("CREATE (a:MOVIE {id: $id})", id=movie["id"])

        # #insertPerson
        # for person in movie["id"]["person"]:



