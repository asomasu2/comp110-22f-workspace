"""Examples of tuples and range sequences."""

# an example of a tuple without type aliasing 
goat: tuple[str, int] = ("MJ", 23)

# Tuples are sequences, so they're 0-indexed
print(goat[0])
print(goat[1])

# Sequences have lengths
print(len(goat))

# Sequences are iterable with for...in loops
# Meaning you can loop over them with for...in loops

for item in goat:
    print(item)

# Tuples, unlike lists, are immutable
# Which means we cannot reassign items, nor append, nor pop, etc
# goat[0] = "LBJ"

# We can "invent" our own type with a type alias
Player = tuple[str, int]

# Once we've aliased a type, we can create variables of that type
the_real_goat: Player = ("Redick", 4)

print(the_real_goat)


# A range is another common sequence type
zero_to_nine: range = range(10)
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i) 


# We can have different steps for more control
odds_to_99 = range = range(1, 100, 2)
