#!/usr/bin/python

def set_cal():
	list1=input("1st list: ")
	list2=input("2nd list: ")
	
	union=set(list1)|set(list2)
	intersection=set(list1)&set(list2)

	union.remove(',')
	union.remove('[')
	union.remove(']')
	intersection.remove(',')
	intersection.remove('[')
	intersection.remove(']')

	union=list(union)
	intersection=list(intersection)

	union=' '.join(union).split()
	intersection=' '.join(intersection).split()
	
	union=list(map(int,union))
	intersection=list(map(int,intersection))

	union.sort()
	intersection.sort()
	
	print("=> union %s" % union)
	print("=> intersection %s" % intersection)


if __name__== '__main__':
	print("this is my_module...")
