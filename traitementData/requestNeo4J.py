#persons =  [("antoine", "ACTOR"), ("nico", "DIRECTOR"), ("nico", "ACTOR")]
def getFilms(persons):
    request = "MATCH "
    for idx, person in enumerate(persons):
        request += "(n:MOVIE)-[:"+ person[1] + "]-(:PERSON{id:" + str(getIDFromMongo(person[0])) + "}),"
    request = request[:-1]
    request += " return n"
    return request

def getNearestPerson(name, distance):
    request = "MATCH (o:PERSON{id:" + str(getIDFromMongo(name)) + "})-[*0.." + str(distance) + "]-(p:PERSON) return p"
    return request

def getNearestFilms(name, distance):
    request = "MATCH (o:MOVIE{id:" + str(getIDFromMongo(name)) + "})-[*0.." + str(distance) + "]-(p:MOVIE) return p"
    return request