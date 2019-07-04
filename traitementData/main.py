from pymongo import MongoClient
from utils import *
import json
from imdb import IMDb
import xmljson
from xml.etree.ElementTree import fromstring


if __name__ == "__main__":

    collection1 = MongoClient('mongodb://localhost:27017/').linkdin.collection1

    ret = {"allMovies":[]}

    ia = IMDb()
    base = None

    #foreach movie id
    for i in range(12000, 12500):

        try:
            print(i)
            film = ia.get_movie(i)
            film = film.asXML()

            xml = fromstring(film)

            tmpJSON = xmljson.badgerfish.data(xml)
            tmpSTR = json.dumps(tmpJSON).replace("$", "do_")
            tmpJSON = json.loads(tmpSTR)

            ret["allMovies"].append(tmpJSON)
            #insert(collection1, tmpJSON)

        except:
            print("erreur", i)


    with open('films.json', "w") as f:
        print(json.dumps(ret), file=f)

