
#TODO: make for waternsw data
import pickle
from os import path

filename = "cache.p"

# locations should be a dictionary wzId -> amphoraId
def water_save(locations):
    #locations.update(wz_locations())
    pickle.dump( locations, open( filename, "wb" ) )

def water_load():
    if path.exists(filename):
        locations = pickle.load( open( filename, "rb" ) )
        return locations
    else:
        return {}
