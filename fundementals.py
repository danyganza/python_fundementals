my_num = 5.6
my_string = 'Hello World'
my_bool = False


print(my_num)
print(my_bool)
print(my_string)


if (my_num > 10):
    print('That is larger than 10')
else:
    print('That is not larger than 10')

if (my_num < 0 and my_bool == True):
        print('Negative and True')
elif (my_num >= 0 and my_bool == False):
        print('Posive and false')
elif (my_num > 100 or my_bool == True):
        print('Large or True')
else:
        ("I don't know")

my_strings = ['this is the first string','this is the second string', 'this is the third string']
my_nums = [1, 2, 3, 4, 5, 6]

for strings in my_strings:
        print('string')

for num in my_nums:
        print(f'look at this sumber: {num}')

def static_greeting():
        print('Hello Danny')

static_greeting()

def dynamic_greeting(name):
    print(f'Hello {name}')

dynamic_greeting('Dale')
dynamic_greeting('Alice')
dynamic_greeting('Ganza')

def find_treasure(to_search):
    for test in to_search:
       if(test == 'tresure'):
              return True
       return False

strings_one = ['one', 'treasure', 'three']
contains_treasure = find_treasure(strings_one)
print(contains_treasure)
