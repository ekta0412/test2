#water:-water.mp3
#eyes:eye.mp3--------done-----every30min
#physical activity: phy.mp3-------every 45 min
#9-5
#3.5 liters

#pygame

#import pygame
import time
#a=time.localtime(time.time())
#print(a)

a=time.strftime("%H : %M :%S")
print("Current time is :",a)

def water():
    b=0
    for i in range(a):
        print("Did u Drink water: Please enter y or n")
        a=input()
        if a == "y":
            b = b+1
        else:
            print("Drink in next hour")
            continue

    return b

c=water()

print("You drank",c,"glasses of water")