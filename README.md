# pi-pir
A Raspberry Pi Motion Camera based on Raspberry Pi Camera module and a simple PIR sensor

Motion detection using a pir sensor on a raspberry pi. 
====================================================================================

This way a little motion sensor camera that takes photo and sends it as an email is created.

Ingredients:

1)Raspberry Pi (any model should do the work) with Raspbian on any other debian like OS (or else you should use mjpeg shell script in different way)


2)Raspberry Pi Camera (enabled)


3)A pir sensor with it's data pin connected to GPIO pin 4 or any other if change the sensor variable on pir.py


4)An smtp email account set up on the pir.py


5)Internet connection for the Raspberry Pi


6)Enjoy!

Usage
=====
Simply run python pir.py OR make pir.py executable an run it in command line as ./pir.py

Authors
=======

Dimitris Andritsakis


License
=======

pir.py is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.
