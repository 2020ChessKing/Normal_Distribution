# imports
import pandas, statistics as stats, math, csv, plotly.figure_factory as ff, plotly.express as px
from plotly import graph_objects as go

# code
framed_data = pandas.read_csv(r"C:\Swarup\WhiteHat Jr\Python\Projects\Normal_Distribution\data.csv")
graph = ff.create_distplot([framed_data["Avg Rating"].tolist()], ["Rating"], show_hist=False)
graph_ratings_mean = stats.mean(framed_data["Avg Rating"])
graph_ratings_mode = stats.mode(framed_data["Avg Rating"])
graph.add_trace(go.Scatter(x=[graph_ratings_mean, graph_ratings_mean], y=[0, 0.7], mode="lines", name="Average Rating"))
print(graph_ratings_mean, graph_ratings_mode)
graph.show()
