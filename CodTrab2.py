import sys #modificação feita pelo aluno

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import datetime
import matplotlib.pyplot as plt

datas = pd.read_csv(open(sys.argv[1])) #modificação feita pelo aluno

datelist = datas.enddate.tolist()

datelist = [datetime.datetime.strptime(date,'%m/%d/%Y')for date in datelist]
datelist = ['%d-%02d' %(date.year,date.month)for date in datelist]

months = np.array(datelist)
unique_months = np.unique(months)

results = []

for month in unique_months:
    
    rawpoll_trump_sum = datas.rawpoll_trump[months==month].sum()
    rawpoll_clinton_sum = datas.rawpoll_clinton[months==month].sum()
    
    results.append((month,rawpoll_trump_sum,rawpoll_clinton_sum))

months,rawpoll_trump_sum,rawpoll_clinton_sum = zip(*results)

plt.plot(rawpoll_trump_sum,color='b')
plt.plot(rawpoll_clinton_sum,color='r')
plt.show()
