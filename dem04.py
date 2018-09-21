import random

aum =[]
while len(aum)<5:
    r = random.randint(1,5)
    if not r in aum:
        aum.append(r)

print(aum)





