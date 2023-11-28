#Nelson Hucklebridge
#100614680
#tprg 2131-01
#2023-11-28
#This program transfers varios vcgencmds as JSON objects too a client on pc
#ref https://www.nicm.dev/vcgencmd/, https://openai.com/chatgpt
import socket
import os, time
import json
import vcgencmd
s = socket.socket()
host = '' # Localhost
port = 5000#port being used
s.bind((host, port))
s.listen(5)


#gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
t = os.popen('vcgencmd measure_volts ain1').readline()#gets from the os, using vcgencmd - the core-temperature
q = os.popen('vcgencmd measure_clock arm').readline()#gets from the os, using vcgencmd - the clock arm
p = os.popen('vcgencmd measure_clock hdmi').readline()#gets from the os, using vcgencmd - the clock hdmi
b = os.popen('vcgencmd codec_enabled  mpg4').readline()#gets from the os, using vcgencmd - the mpg4 enable
v = os.popen('vcgencmd get_mem  arm').readline()#gets from the os, using vcgencmd - memory arm
print(q, p, b, v )
# initialising json object string
ini_string = """{
                "Temperature":t,
                "ARM": q,
                "HDMI": p,
                "mpg4" : b,
                "memARM" : v }"""
# converting string to json
f_dict = eval(ini_string) # The eval() function evaluates JavaScript code represented as a string and returns its completion value.
#used chatgpt as a learning tool for next line:
f_output= "\n".join([f"{key}: {value}" for key, value in f_dict.items()])#seperates string into seperate lines
# vcgencmd measure_volts 2711
if __name__ == "__main__":#name guard too exit gracefully
    try:
        while True:
          c, addr = s.accept()
          print ('Got connection from',addr)
          res = f_output.encode('utf-8') # needs to be a byte and encoded
          c.send(res) # sends data as a byte type
          c.close()
    except KeyboardInterrupt:#exits using CTRL-C
        print("exiting")
