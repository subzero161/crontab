#  Import Packages
import os 
import sys
import time
import csv
import pandas as pd
import crontab

# get the current time
now = time.time()
timestart = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', timestart)

# get current working directory
cwd = os.getcwd()

# print cws
print(cwd)

# create a new dictionary with dummy data
earthquake_df = pd.read_json('https://earthquake.usgs.gov/fdsnws/event/1/application.json')
earthquake_df

# save data to a local csv file
earthquake_df.to_csv('data/earthquake_data.csv', index=None)

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/crontabFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(earthquake_df))

