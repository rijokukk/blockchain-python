def print_data(param1, param2):
    print(param1 + " " + param2)


def number_of_decades(age):
    return age // 10


name = input('Your name: ')
age = input('Your age: ')
print_data(name, age)
print("You have already lived " + str(number_of_decades(int(age))) + " decades!")