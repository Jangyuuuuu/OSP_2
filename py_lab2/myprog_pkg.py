#!/usr/bin/python
from my_pkg.bin_cal import *
from my_pkg.set_cal import *

if __name__== '__main__':
	while(True):
		str=input("Select menu: 1)conversion  2)union/intersection  3)exit ? ")

		if str=='1':
			bin_cal()
			continue
		elif str=='2':
			set_cal()
			continue
		else:
			print("exit the program...")
			break
