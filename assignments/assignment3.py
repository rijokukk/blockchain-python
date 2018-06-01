# 1)
persons = [
    {
    'name': 'Riku',
    'age': 25,
    'hobbies': [
        'Computers',
        'Discgolf'
        ]
    }, {
    'name': 'Orc',
    'age': 100,
    'hobbies': [
        'Killing hobbits',
        'Eating meat'
        ]
    }, {
    'name': 'Jarska',
    'age': 10,
    'hobbies': [
        'Drawing'
        ]
    } 
]

# 2)
person_names = [person['name'] for person in persons]
print(person_names)

# 3)
person_ages = [person['age'] for person in persons]
print(all([el > 20 for el in person_ages]))

# 4)
persons_copy = [person.copy() for person in persons]
persons_copy[0]['name'] = 'Jau'
print(persons_copy)
print(persons)

# 5)
riku, orc, jarska = persons
print(riku)
print(orc)
print(jarska)