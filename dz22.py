import numpy as np
import pandas as pd
data_set = pd.read_csv("C:/Users/Xyexx/Downloads/Telegram Desktop/2.4 houses.csv")
print(data_set[15:18])
#b= "имя:"
#data_set.Name = "2.4 дома"


data_set = data_set.dropna()
print(data_set.info)
print(data_set.describe)
#print(data_set.dtypes)
#print(data_set.head(5))
print(data_set.index)
print(data_set[[ "YearBuilt", "Neighborhood","YearRemodAdd"]].sort_values([ "YearBuilt","Neighborhood","YearRemodAdd"], ascending=False).head(10))