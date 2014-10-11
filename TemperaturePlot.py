"""
    TemperaturePlot.py - Indoor V.S. Outdoor Temperature Plotter

	Copyright 2014 Carter Yagemann

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    A copy of this license is available at <http://www.gnu.org/licenses/>.
"""

########################################################
##                  Temperature Plot                  ##
########################################################

## Libraries
##------------------------------------------------------
import json, requests, sys, time
from datetime import datetime

## Constants
##------------------------------------------------------
url = 'https://api.spark.io/v1/devices/DEVICE_ID/temp_f'
token = 'ACCESS_TOKEN'
weather_api = 'http://api.openweathermap.org/data/2.5/weather?q=CITY,STATE&mode=json&units=imperial'

## Methods
##------------------------------------------------------
def getTemp():
  params = dict(access_token=token)
  resp = requests.get(url=url, params=params)
  data = json.loads(resp.text)

  try:
    temp = round(data['result'], 1)
  except:
    temp = 0.0

  return temp

def getWeather():
  resp = requests.get(url=weather_api)
  data = json.loads(resp.text)

  try:
    temp = round(data['main']['temp'] , 1)
  except:
    temp = 0.0

  return temp

def printUsage():
  print "python tempPlot.py <minute_interval> <number_of_data_points>"

## Main Loop
##------------------------------------------------------
if len(sys.argv) != 3:
  printUsage()
  sys.exit()

try:
  interval = int(sys.argv[1]) * 60
  count = int(sys.argv[2])
except:
  print "Failed to parse parameters"
  printUsage()
  sys.exit()

fileName = "output." + str(datetime.now()) + ".csv"
file = open(fileName, 'w')
file.write("datetime, room_temp, outdoor_temp\n")

for x in range(0, count):
  temp = getTemp()
  weather = getWeather()
  file.write(str(datetime.now()))
  file.write(", ")
  file.write(str(temp))
  file.write(", ")
  file.write(str(weather))
  file.write('\n')
  time.sleep(interval)

file.close()
