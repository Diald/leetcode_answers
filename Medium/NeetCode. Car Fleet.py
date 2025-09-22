'''n cars - 
heading towards target
cars can not overtake
if a faster car catches up to the slower car, the faster cars slows down and travels together with the slower one. 
cars that end up travelling together in such a way is called a fleet. 


example - 
target = 12 #target position 
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]


starting with the car closest to the target, since it can not be blocked by anyone, it will be a separate fleet. we would calculate the time of each. if the car behind arrive earlier than or equal to that blocker time / the car which is closest to target. they will join its fleet.
but if the car behind it cant reach on time as the faster one and its time is strictly greater than the fastest fleet or car then it forms a new fleet. since both of them just can't meet. 

sort positions in descending order - 
[10, 8, 5, 3, 0]
Their times - 
[1, 1, 7, 3, 12]
'''

def carFleet(target, position, speed):
    n = len(position)
    if n==0:
        return 0 
    
    times = []
    for i in range(n):
        timeI = (target - position[i])/speed[i]
        times.append((position[i], timeI))
    
    times.sort(key= lambda x: x[0], reverse = True)
    
    fleetSize = 0
    blockTime = 0.0
    
    for pos, time in times:
        if(time > blockTime):
            fleetSize +=1
            blockTime = time
            
    return fleetSize 
    
    
    
