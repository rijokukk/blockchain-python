import json
import pickle

print('-' * 20)
print("Enter the text you want to be written in file.")
print("You can print the texts in file with command: PRINT")
print("You can quit program with command: QUIT")
print('-' * 20)

waiting_for_input = True
user_inputs = []

with open('user_inputs.txt', mode='r') as f:
    file_content = f.readlines()
    user_inputs = json.loads(file_content[0])

with open('user_inputs.p', mode='rb') as f:
    user_inputs = pickle.loads(f.read())

while waiting_for_input:
    user_input = input('Your text: ')
    if user_input == 'QUIT':
        waiting_for_input = False
        continue
    elif user_input == 'PRINT':
        with open('user_inputs.txt', mode='r') as f:
            file_content = json.loads(f.read())
            print('-' * 20)
            for line in file_content:
                print(line)
            print('-' * 20)
        with open('user_inputs.p', mode='rb') as f:
            file_content = pickle.loads(f.read())
            print(file_content)
            print('-' * 20)
        continue

    user_inputs.append(user_input)

    with open('user_inputs.txt', mode='w') as f:
        f.write(json.dumps(user_inputs))

    with open('user_inputs.p', mode='wb') as f:
        f.write(pickle.dumps(user_inputs))