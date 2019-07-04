from pymongo import MongoClient
from utils import *
import json
from imdb import IMDb
import xmljson
from xml.etree.ElementTree import fromstring
import config as cfg


if __name__ == "__main__":

    collection1 = MongoClient(cfg.mongoServer).movies.persons
    ret = {"allMovies":[]}

    ia = IMDb()
    base = None

    print("before loop")

    #foreach movie id
    for i in range(cfg.idMin, cfg.idMax):

        try:
            print(i)
            film = ia.get_movie(i)
            film = film.asXML()

            xml = fromstring(film)

            tmpJSON = xmljson.badgerfish.data(xml)
            tmpSTR = json.dumps(tmpJSON).replace("$", "do_")
            tmpJSON = json.loads(tmpSTR)

            ret["allMovies"].append(tmpJSON)
            print("before insert collection")
            insert(collection1, tmpJSON)
            print("after insert collection")

        except:
            print("erreur", i)


    with open('films.json', "w") as f:
        print(json.dumps(ret), file=f)

