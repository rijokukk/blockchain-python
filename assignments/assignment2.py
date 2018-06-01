names = ['Aku', 'Tupu', 'Hupu', 'Lupu', 'Naakka', 'Apinaorkesteri', 'Karhukopla', 'Nipa']

for name in names:
    if len(name) > 5 and ('n' in name or 'N' in name):
        print(len(name))

print(names)

not_empty = True
while not_empty:
    if len(names) < 1:
        not_empty = False
        continue
    names.pop()

print(names)
