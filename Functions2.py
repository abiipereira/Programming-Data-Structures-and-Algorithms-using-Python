'''
 For an expression with parentheses, we can define the nesting depth as the maximum number of parentheses that are open when reading the expression from left to right.
 For instance, the nesting depth of "(33+77)(44-12)" is 1, while the nesting depth of "(a(b+c)-d)(e+f)" is 2.
 Write a Python function depth(s) that takes a string containing an expression with parentheses and returns an integer, the nesting depth of s.
 You can assume that s is well-parenthesized: that is, that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it.
'''
def depth(s):
 max=0
 counter=0
 i=0
 while i<len(s):
   if s[i]=="(" :
    counter=counter+1
   if s[i]==")" and counter!=0:
    counter=0
   if counter>max:
    max=counter
   i=i+1
 return (max)