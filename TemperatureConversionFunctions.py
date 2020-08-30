# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:40:10 2020

@author: Senthil-Malli
"""


# Initializing variables
x=0
x = input ("Choose 1 to convert from Farenheit to Celius; Choose 2 to convert from Celsius to Farenheit: ")
x = int(x)

def Farenheit_Celsius():
    # Intializing variables
    f=0
    c=0
    f = input ("Enter the temperature in Farenheit: ")
    f = int(f)
    c = (f-32)*5/9
    c = int(c)
    print("Temperature in Celius: {}".format(c))
    
def Celsius_Farenheit():
    # Intializing variables
    f=0
    c=0  
    c = input ("Enter the temperature in Celius: ")
    c = int(c)
    f = c/5*9+32
    print("Temperature in Farenheit: {}".format(f))

# to convert from Farenheit to Celsius
if (x==1):
    Farenheit_Celsius()
    
# to convert from Celsius to Farenheit
if (x==2):
    Celsius_Farenheit()