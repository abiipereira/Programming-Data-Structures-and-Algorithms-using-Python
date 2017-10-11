'''
    In this task you will given a word and you must find the longest subword of this word that is also a palindrome.
    For example if the given word is abbba then the answer is abbba. 
    If the given word is abcbcabbacba then the answer is bcabbacb.
'''

n=input()
text=input()
results = []
maxi='a'
for i in range(len(text)):
        for j in range(0, i):
            part = text[j:i + 1]

            if part == part[::-1]:
                results.append(part)

for i in range(0,len(results)):
 if len(results[i])>=len(maxi):
      maxi=results[i]
print (len(maxi))      
print (maxi)