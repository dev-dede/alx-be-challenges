import random

random_numbers = []
for i in range(15):
    random_numbers.append(random.randint(1, 7))
print(random_numbers) #This is a list meaning its mutable, ordered and has duplicates

#Converting to set to remove duplicates
unique_numbers = set(random_numbers)
print(unique_numbers)