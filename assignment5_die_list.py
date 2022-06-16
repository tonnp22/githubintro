import random

count = [0, 0, 0, 0, 0, 0]
for x in range(600):
    die = random.randint(1, 6)  # put this INSIDE For loop to roll die 600 times
    count[die-1] += 1

for x in range(6):
    # literal = Num of times 1 was rolled
    #  = Percentage is %
    print("Num of times side", x + 1, "was rolled:", count[x])
    print("Percentage is: {:.2f}%".format((count[x]/600)*100))

print("Good bye!")
