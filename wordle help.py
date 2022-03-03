from collections import Counter
import re

words=[]

with open('wordle words.txt', 'r') as www:
    for w in www:
        words.append(w.strip())

potlst=[]
potstr=''

counter = 0

for x in words:
    if all(z not in x for z in 'atiwed') and all(z in x for z in 'runo') and \
    re.match('[^ru][^n][a-z][a-z][^o]', x):
        #x[0] != 'r' and x[2]=='a' and x[4]=='e':# and x[4]!='l':
        print(x, end=', ')
        counter += 1
        y=''
        for z in x:
            if z not in y:
                y += z
        potstr += y

a = Counter(potstr)
print()
print(counter, 'words,', a)

for x in words:
    if all(z in x for z in 'endw'):
        print(x, end=', ')

# triple=[]

# for x in words:
#     for y in x:
#         if x.count(y) >2 and x not in triple:
#             triple.append(x)
# print(', '.join(triple))

# two_dist=[]

# for x in words:
#     y=''
#     for z in x:
#         if z not in y:
#             y+=z
#     if len(y)<=2:
#         two_dist.append(x)

# print(two_dist)

# no_vowels=[]

# for x in words:
#     y='aiueo'
#     if all(z not in x for z in y):
#         no_vowels.append(x)
# print(', '.join(no_vowels))

# xxx=[]

# for x in words:
#     if 'x' in x:
#         xxx.append(x)
# print(', '.join(xxx))

# no_common=[]

# for x in words:
#     y='esiarntol'
#     if all(z not in x for z in y):
#         no_common.append(x)
# print(', '.join(no_common))
