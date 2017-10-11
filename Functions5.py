'''
   A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values.  
   The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.
   Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.
'''
def valley(l):
    i=0
    count1=0
    count2=0
    while i<len(l)-1:
      if l[i]>l[i+1]:
        count1=count1+1
        i=i+1
      elif count1>=1 and l[i]<l[i+1]:
        count2=count2+1
        i=i+1
      else:
        return (False)
        
    if count2>=1:
      return (True)
    else:
      return (False)
        
