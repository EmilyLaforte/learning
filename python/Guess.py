import turtle

import random

##n=random.randint(1, 20)
##g=0
##while(g !=n):
##    g=input("Quel est ce nombre? ")
##    g=int(g)
##print("Correct!")


n=random.randint(1, 2000)
g=0

while g !=n:
    g=input("Quel est ce nombre? ")
    
    g=int(g)
    if(g>n):
        print("Non idiot")
    if(g<n):
        print("Non idiot")
print("Correct!")
