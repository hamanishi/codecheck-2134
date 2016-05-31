#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot():
  #ここに素数判定プログラムを実装してください。
  def __init__(self, data):
    self.command = data["command"]
    self.data = data["data"]
    
  def generate_hash(self):
    print("aho")
    print(self.command)
    #for i in xrange(len(self.command)):
    #  num += ord(self.command[i])
     # print(num)
    num_string = ""
    for char in self.command:
      num_string += str(ord(char))
      print(num_string)
    
    if len(num_string) >= 22:
      print("aho")
      result = ""
      result = str(self.scientificNotation(float(num_string)))
      print(result)
      result.replace("e+","")
      print(result)
      self.hash = int(num_string, 16)
      print(self.hash) 
      
    else :
      print("boke")
      self.hash = int(num_string, 16)
      print(self.hash)
      
  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself
  def scientificNotation(self, num):
    data = "%.16e" % num
    result = data if (int(data.split("e+")[1]) > 20) else num
    return result
  
