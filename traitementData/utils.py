def insert_one(collection, dictionnaire):
    collection.insert_one(dictionnaire)

def insert(collection, dictionnaire):
    collection.insert(dictionnaire)

def insertMovieInformation(database, movie):

   # print({ key:value for key, value in movie.items() if key != "person"})
    database.movies.insert({ key:value for key, value in movie.items() if key != "person"})


def insertPersonInformation(database, movie):

    #print({key: value for key, value in movie.items() if key == "person"})
    database.persons.insert({ key:value for key, value in movie.items() if key == "person"})


# def add_movie(id):
#     graph.run("CREATE UNIQUE (a:Movie {id: $id})", id=id)


