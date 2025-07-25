def lemonade_change(arr):
    fives = 0
    tens = 0
    for i in arr:
        if(i==5):
            fives+=1
        elif(i==10):
            if(fives>=1):
                fives-=1
                tens+=1
            else:
                return False
        elif(i==20):
            if(fives>=3):
                fives-=3
            elif(fives>=1 and tens>=1):
                fives-=1
                tens-=1
            else:
                return False
    return True

print(lemonade_change([5, 5, 5, 10, 20]))  # Output: True

