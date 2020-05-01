num = int(input("Aposte em um número(1-12): "))
import random
d1=(random.randrange(1, 7))
d2=(random.randrange(1, 7))
print("O primeiro dado foi",d1)
print("O segundo dado foi",d2)
if d1+d2 == num:
    print("Você ganhou!")
else:
    print("Você perdeu a aposta")
