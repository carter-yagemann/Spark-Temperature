Spark Temperature
=================

Overview
--------

Spark Temperature is a simple project which builds off of the 
[temperature demo](http://docs.spark.io/examples/#measuring-the-temperature) spark.io 
includes with their Spark Core micro-controllers. While their demo only goes as far as 
wiring the Spark Core and pushing the temperature readings up to their cloud, this 
project goes a step further and uses Python scripts to display the readings in real 
time as a desktop GUI and to record in a file the readings along with the outdoor 
temperature over time so they can be compared.

Materials
---------

1x Spark Core Micro-controller

1x TMP36 Temperature Sensor

1x 10nF Capacitor (optional)

Details on how to wire the Spark Core micro-controller can be found 
[here](http://docs.spark.io/examples/#measuring-the-temperature).

Dependencies
------------

The Python scripts were written for Python 2.7.8. The only third party library they 
require is the [requests](http://docs.python-requests.org/en/latest/) library.

Files
-----

`temperature.ino` - C source code for the Spark Core micro-controller. Measures the 
temperature and pushes it to Spark.io's cloud.

`DesktopMonitor.py` - Python script which creates a GUI and displays the temperature 
readings from the Spark Core micro-controller. The readings update ever 60 seconds.

`TemperaturePlot.py` - Plots the time, indoor temperature, and outdoor temperature 
as a comma separated value sheet (CSV). See the usage method for details on how to 
set the interval and duration.

`Network Diagram.jpg` - A visual representation of the network layout for the 
`TemperaturePlot.py` script.

`Example Output.csv` - An example output generated using the `TemperaturePlot.py` 
script.

`Example Graph.jpg` - A graph generated using the example output CSV file.