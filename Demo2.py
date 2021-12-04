import pandas as pd
import csv
import plotly.figure_factory as ff
df=pd.read_csv("data1.csv")
figure=ff.create_distplot([df["Sr.No"].tolist()],["MobileBrand"],["AvgRating"],show_hist=False)
figure.show()