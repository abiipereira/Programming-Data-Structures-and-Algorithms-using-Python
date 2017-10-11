'''
   Write a function sumsquares(l) that takes as input a list of integers and retuns the sum of all the perfect squares in l.
   Here are some examples to show how your function should work.
'''

def sumsquares(l):
 sum=0
 for i in l:
  a=i**0.5
  b=int(i**0.5)
  if a==b:
    sum=sum+b*b
 return sum
    
