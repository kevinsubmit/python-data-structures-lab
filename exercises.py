def manage_students():
    students = ['Mary','Bob','John']
    first_student = students[1]
    last_student = students[-1]
    return first_student, last_student


print('Exercise 1:', manage_students())


def combine_foods():
    foods = ('apple','banana','orange','grapes')
    meal = ''
    for food in foods:
        meal += food
    return meal

print('exercise 2',combine_foods())


def slice_foods():
    foods = ('apple','banana','orange','grapes')
    last_two_foods = foods[-2:]
    return last_two_foods

print('exercise 3',slice_foods())


def hometown_info():
    home_town = {
        'city':'shanghai',
        'state':'shanghai',
        'population': 10000000
    }
    home_town_message = f"I was born in {home_town['city']},{home_town['state']}-population of {home_town['population']}"
    return home_town_message

print('exercise 4',hometown_info())



# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    home_town = {
        'city':'shanghai',
        'state':'shanghai',
        'population': 10000000
    }
    home_town_items = []
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())







