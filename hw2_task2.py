#Skylar Olsen
#02/02/2019
#Homework 2 Task 2

import numpy as np
import math as m
import matplotlib.pyplot as plt
"""
Make sure you make this module as modular as you can.
That is add as many functions as you can.
1) Have a main function
2) A function to capture user input, this could be inside your "main" function
3) A function to calculate the projectile motion
4) A function to display the graph

Make sure you use docstring to document your module and all
your functions.

Make sure your python module works in dual-mode: by itself or import to other module
"""
# NOTE: You may need to run: $ pip install matplotlib

x0 = 1.0
vx0 = 70.0         # TODO: capture input

y0 = 0.0
vy0 = 80.0          # TODO: capture input

ax = 0.0
ay = -9.8           # define a constant

delt = 0.1
t = 0.0

x = []
y = []

intervals = 170


def px(x,v,t,a):
       """
       Function to calculate projectile motion
       """
       return x + (v*t) + (0.5*a*t**2)

def plot_data():
       """
       Function to plot data
       """
       plt.plot(x, y)
       plt.show()

def main():
       """
       Main" Function
       """
       capture_input()
       set_data()
       plot_data()


def capture_input():
       """
       Function to get user input
       """
       # define local variables
       global vx0
       global vy0 
       vx = ''
       vy = ''
       
       #get input and validate that it is a digit
       while vx.isdigit() == False:
              vx = input('Enter x Velocity:')
              if vx.isdigit():
                     #set the velocity to the user's input
                     vx0 = int(vx)
              else:
                     print(vx, ' is not a digit')
       
       #get input and validate that it is a digit
       while vy.isdigit() == False:              
              vy = input('Enter y Velocity:')
              if vy.isdigit():
                     #set the velocity to the user's input
                     vy0 = int(vy)
              else:
                     print(vy, ' is not a digit')

def set_data():
       """
       Function to set data
       """

       # loop through array of points
       for i in range(intervals):
              global x,y,t
              x.append(px(x0,vx0,t,ax))
              y.append(px(y0,vy0,t,ay))
              t = t + delt

              if i != 0 and y[i] <= 0.0:
                     break

if __name__ == "__main__":
    # "main" program
    main()
    exit(0)
