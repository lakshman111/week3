# Working with lists
# Helpful links:
# - https://docs.python.org/3/library/functions.html
# - https://docs.python.org/3/library/numeric.html

names_of_planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn', 'Jupiter', 'Uranus', 'Neptune']


# Write code that will display answers to the following questions:
# ----------------------------------------------------------------

# How many planets are there?
# number = len(names_of_planets)
# print("There are", number, "planets")



# Display the names of the planets in alphabetical order
# print(sorted(names_of_planets))
# this does not change the actual array



# Remove a planet from the list
# names_of_planets.remove(names_of_planets[len(names_of_planets) -1])
# print(names_of_planets)




# Add Pluto to our solar system
# names_of_planets.append("Pluto")
# print(names_of_planets)

# OR, if you didn't want to use a method...
# .insert()



# Display the name of a planet chosen at at random (hint: use the "random" library)
# import random
# print(random.choice(names_of_planets))



# Randomize the list
# import random
# random.shuffle(names_of_planets)
# print(names_of_planets)

