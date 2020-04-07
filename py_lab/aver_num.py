#!/usr/bin/python

N=int(input("How many numbers do you want to enter? "))

num=0; sum=0; aver=0;

for i in range(N):
	num=int(input())
	sum+=num

aver=sum/N

print("The average of the numbers is %.1f" % aver)
