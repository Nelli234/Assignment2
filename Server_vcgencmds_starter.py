# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/

import socket
import os, time
import json
import vcgencmd
s = socket.socket()
host = '' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)


#gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
t = os.popen('vcgencmd measure_volts ain1').readline()#gets from the os, using vcgencmd - the core-temperature
q = os.popen('vcgencmd measure_clock arm').readline()
p = os.popen('vcgencmd measure_clock hdmi').readline()
b = os.popen('vcgencmd codec_enabled  mpg4').readline()
v = os.popen('vcgencmd get_mem  arm').readline()
print(q, p, b, v )
# initialising json object string
ini_string = """{
                "Temperature":t, "ARM": q,
                "HDMI": p,
                "mpg4" : b,
                "memARM" : v }"""
# converting string to json
f_dict = eval(ini_string) # The eval() function evaluates JavaScript code represented as a string and returns its completion value.
for key, value in f_dict.items():
    m = f"{key}: {value}"
    print(m)
# vcgencmd measure_volts 2711
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  res = bytes(str(m), 'utf-8') # needs to be a byte
  c.send(res) # sends data as a byte type
  c.close()
