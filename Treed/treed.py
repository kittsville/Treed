import cson

def ingest(filename):
    with open(filename, 'rb') as file:
        recipeObject = cson.load(file)

    return recipeObject
