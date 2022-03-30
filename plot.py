import pandas as pd 
import plotly.figure_factory as ff
import csv
import scipy

df = pd.read_csv('data.csv')
fig = ff.create_distplot([df["Avg Rating"].to_list()], ["Average mobile rating"], show_hist = True)
fig.show()
