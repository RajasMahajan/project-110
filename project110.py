import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff  
import random
import plotly.graph_objects as go
df = pd.read_csv('data.csv')
data = df['reading_time'].tolist()

def findmean(times):
    dataone = []
    for i in range(0,times):
        randomone = random.randint(0,len(data)-1)
        value = data[randomone]
        dataone.append(value)
    mainmean = statistics.mean(dataone)
    return mainmean

def plotlygraph(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([df],['reading_time'], show_hist =False)
    fig.add_trace(go.Scatter(x =[mean,mean], y =[0,1] , mode='lines', name ='mean'))
    fig.show()

def setup():
    mean_list= []
    for i in range(0,100):
        randommean = findmean(100)
        mean_list.append(randommean)
        plotlygraph(mean_list)

setup()




