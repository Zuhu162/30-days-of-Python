animals = ['lion', 'tiger', 'hippo', 'monkey', 'tiger']
uniques = []

for animal in animals:
    if animal not in animals:
        uniques.append(animal)

print(uniques)