/*
 * temperature.ino - Temperature Sensor for Spark Core
 *
 * Copyright 2014 Carter Yagemann
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * A copy of this license is available at <http://www.gnu.org/licenses/>.
 */

/* Global Variables */
double temp_c = 0.0;
double temp_f = 0.0;

/* Prototypes */
double read_temp();
double cnvrtcf(double);

void setup() {
  // Register with spark cloud
  Spark.variable("temp_c", &temp_c, DOUBLE);
  Spark.variable("temp_f", &temp_f, DOUBLE);

  // Temperature guage is attached to analogue 7
  pinMode(A7, INPUT);
}

void loop() {
  temp_c = read_temp();
  temp_f = cnvrtcf(temp_c);
  // Delay for 100ms
  delay(100);
}

/*
 * Reads the temperature and returns it as a double. Value is in Celsius.
 */
double read_temp() {
    
    int reading = analogRead(A7);
    double voltage = (reading * 3.3) / 4095;
    return (voltage - 0.5) * 100;
}

/*
 * Converts C to F.
 */
double cnvrtcf(double c) { return (c * (9.0 / 5.0) + 32); }