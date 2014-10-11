"""
    DesktopMonitor.py - Spark Temperature Desktop Display

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

## Libraries
##------------------------------------------------------
import json, requests
from Tkinter import Tk, Label

## Constants
##------------------------------------------------------
url = 'https://api.spark.io/v1/devices/DEVICE_ID/temp_f'
token = 'ACCESS_TOKEN'

## Scripts
##------------------------------------------------------
def getTemp():
  params = dict(access_token=token)
  resp = requests.get(url=url, params=params)
  data = json.loads(resp.text)
  try:
    temp = round(data['result'], 1)
  except:
    temp = "N/A"
  try:
    tempLabel.config(text=str(temp))
  except:
    print "Callback error"
  tempLabel.after(60000, getTemp)
  
## Main Method
##------------------------------------------------------
mainWindow = Tk()
mainWindow.title("Spark Temperature")
tempLabel = Label(mainWindow, text="N/A", font=("Helvetica", 92, "bold"),
                  pady=20, padx=20, foreground='#fbfeff',
                  background='#3d76dd')
getTemp()
tempLabel.pack()
mainWindow.mainloop()