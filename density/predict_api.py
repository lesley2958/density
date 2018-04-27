import json
def api_all_buildings (df):
    building_divs = {}

    #  building = index of row (String)
    #  predictions = Series of columns with predictions

    for building, predictions in df.iterrows():
        #  create plot prediction for each building and add to dictionary
        building_divs[building] = json.dumps(
            [{"time":time, "prediction": prediction} for time, prediction in zip (predictions.index.tolist()[::4], predictions[::4] * 100)])

    #  create script and div from dictionary
    return building_divs