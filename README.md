# Arduino-Python USB Communication (Arduino to Python and Python to Arduino)

This repository contains a system that simplifies reading and sending data through USB to Arduino. I searched a lot for these code but didn't find any so I created this repo to remember how it is done. Note that the provided code expects that only one line is sent from the Arduino at a time. If there are multiple lines, they are added to a string and outputted all at once.


### Prerequisites

- Python 3.x
- PySerial library
- Arduino IDE or PlatformIO
<br>

To install the PySerial library, use the following command:

```sh
pip install pyserial
