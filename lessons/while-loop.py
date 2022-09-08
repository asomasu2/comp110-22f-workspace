"""Practice with loops"""

counter: int = 0
maximum: int = int(input("what do you want to count to? "))
while counter < maximum:
    counter_squared: int = counter ** 2
    print("the square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1

print("done")
