woord = "Hello World"
print(f"Volledige woord --> {woord}")
print(f"woord[2] --> {woord[2]}")
print(f"woord[-7] --> {woord[-7]}")

# concatenation
woord1 = "Howest"
woord2 = "rules"
samen = woord1 + " " + woord2
print(samen)

# string repitition
slogan = woord1 * 4
print(slogan)

# string indexing
letter = woord1[0]
print(letter)

# string slicing
deel_woord = woord1[0:3]
print(deel_woord)

# length string
print(f"Lengte: {len(woord1)}" )
