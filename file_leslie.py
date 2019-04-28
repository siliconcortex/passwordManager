import pickle

def initialize(filename):
    try:
        dictionary = pickle.load(open("database.pickle", "rb"))
    except (OSError, IOError) as handle:
        dictionary = {'key' : 'data' }
        pickle.dump(database, open("database.pickle", "wb"))

def load(filename):
    with open(filename,'rb') as handle:
        data = pickle.load(handle)
    return data

def save(filename, data):
    with open(filename, 'wb') as handle:  
        pickle.dump(data, handle)
    print('Saved.')
    return None
