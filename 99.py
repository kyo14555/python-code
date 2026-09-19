"""
i=1 
while i<10:
    j=1
    while j<=i:
        print(f"{i}*{j}={i*j}\t",end='')
        j+=1
    i+=1
    print()
"""

"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}\t",end='')
    print()
"""

money=10000
for staff in range(1,21):
    import random
    score=random.randint(1,10)
    print(staff,score)
    if money==0:
        print("out of money")
        break
    else:
        if score<5:
            print("not up to standard")
            continue
        else:
            print("up to standard,pay 1000")
            money-=1000


