import random
import time

rnNumber = random.random()
print(rnNumber)

rnInt = random.randint(1, 10)
print(rnInt)

uniqueVal = (time.time() + rnNumber)
print(uniqueVal)