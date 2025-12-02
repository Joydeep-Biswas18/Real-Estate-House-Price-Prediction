import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None



def get_location_names():
    return __locations

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)
def load_save_artifacts():
    global __data_columns
    global __locations

    with open("./Artifacts/Columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./Artifacts/Banglore_home_Prices_model.pickle",'rb') as f:
        __model = pickle.load(f)

if __name__ == "__main__":
    load_save_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st phase JP Nagar",1200,2,2))
    print(get_estimated_price("1st phase JP Nagar",1200,3,3))
    print(get_estimated_price("Kolkata",1200,2,2))