from pymongo import MongoClient
from utils import *
from cleanIMBD import *
import json
from imdb import IMDb
import xmljson
from xml.etree.ElementTree import fromstring
from config import *
from py2neo import Graph

#Instance variables mongoDB
client = MongoClient('localhost', 27017)
database = client.myMovies
movies = database.movies
persons = database.persons

#Get id for a movie
print(getIdFromTitle(movies, "The Broadway Bride"))

#Get id for a person
print(getIdFromName(persons, "Earle Williams"))