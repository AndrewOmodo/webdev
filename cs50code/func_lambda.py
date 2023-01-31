people = [
    {'name': 'John', 'house': 'LA'},
    {'name': 'Peter', 'house': 'Vegas'},
    {'name': 'Andrew', 'house': 'San Diego'},
]
#define a function which will be used to sort the list
# def f(person):
#     return person['name']
# people.sort(key=f)
# or we do it as shown below

people.sort(key=lambda person:person['name'])

print(people)