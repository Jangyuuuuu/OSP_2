#!/usr/bin/python

def bin_cal():
	value=int(input("input binary number: "), 2)
	print("=> OCT>", format(value,'o'))
	print("=> DEC>", format(value,'d'))
	print("=> HEX>", format(value,'x').upper())

if __name__== '__main__':
	print("this is my_module...")
