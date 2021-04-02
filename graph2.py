import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics

list1 = []
dataf = pd.read_csv('./data.csv')
list1 = dataf["Weight(Pounds)"].tolist()


figure = ff.create_distplot([list1],["Weight"])
#figure.show()


mean = statistics.mean(list1)
median = statistics.median(list1)
mode = statistics.mode(list1)

std = statistics.stdev(list1)

list2 = []
for i in list1:
    if(i >= (mean - 1*std) and i <= (mean + 1*std)):
        list2.append(i)

percent = (len(list2)/len(list1))*100
print(percent)