import pickle

def price_prediction(data):
    model_path = "RF_Model.pkl"
    loaded_model = pickle.load(open(model_path, "rb"))

    # "data" is a row of input values:
    y_pred = loaded_model.predict(data)
    return y_pred[0]

# price_prediction(data)

# # -----------------TEST--------------------
# import pandas
#
# # Loading the Data:
# energy_data = pandas.read_csv(r"energy_dataset.csv")
#
# # Dropping Nan values and empty columns:
# energy_data = energy_data.drop("generation fossil coal-derived gas", axis=1)
# energy_data = energy_data.drop("generation fossil oil shale", axis=1)
# energy_data = energy_data.drop("generation fossil peat", axis=1)
# energy_data = energy_data.drop("generation hydro pumped storage aggregated", axis=1)
# energy_data = energy_data.drop("generation wind offshore", axis=1)
# energy_data = energy_data.drop("forecast wind offshore eday ahead", axis=1)
# energy_data = energy_data.drop("generation geothermal", axis=1)
# energy_data = energy_data.drop("generation marine", axis=1)
# energy_data.dropna(axis=0, inplace=True)
# energy_data.reset_index(inplace=True)
# energy_data.drop("index", axis=1, inplace=True)
#
# # Dividing into Test Dataset:
# test_data = energy_data.copy()
# test_data.drop("time", axis=1, inplace=True)
#
# y = test_data["price actual"]
# test_data.drop("price actual",axis=1, inplace=True)
# X = test_data
#
# # Calling the Model on the Test Data:
# index = 25000
# print(price_prediction(X.iloc[[index]]))
