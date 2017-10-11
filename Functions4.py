'''
   Define a Python function ascending(l) that returns True if each element in its input list is at least as big as the one before it.
   Here are some examples to show how your function should work.
'''
def ascending (l):
  i=0
  while i<len(l)-1:
    if l[i]>l[i+1]:
      break
    else:
      i=i+1
  if i==len(l)-1:
   return (True)
  else:
    return (False)
  
