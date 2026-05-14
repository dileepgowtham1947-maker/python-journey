## Day 5  : 30 Days of python programming

## Exercises: Level 1


Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Unpack siblings and parents from family_members




## MY CODE FOR EXERCISE 1 PROBLEMS


tple = tuple()

sisters = ("Deepika", "Sonu", "Laddu", "Elina", "Rosy", "Mary")
brothers = ("Nihaan", "Avyukt", "Pani", "Gowtham", "Sohan")

siblings = sisters + brothers
print(f"Siblings : ", siblings)
print(len(siblings))

family_mem = siblings + ("Ramesh", "Varalakshmi")
print(family_mem)

father, mother, *siblings = family_mem
print("Father :", father)
print("Mother :", mother)
print("Sibligns", siblings)


## Exercises: Level 2
## Day 5  : 30 Days of python programming


Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_stuff_lt list
Delete the food_stuff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')




## MY CODE FOR EXERCISE 2 PROBLEMS


fruits = ("Apple", "Orange", "Banana", "Grape", "Mango")
veg = ("Potato", "Tomato", "Onion", "Spinach","Garlic")
animal_pro = ("Meat", "Milk", "Eggs", "Honey")

food_stuff_tp = fruits + veg + animal_pro
print("Food_Stuff_TP :", food_stuff_tp)

print(list(food_stuff_tp))
print(len(food_stuff_tp))

middle = len(food_stuff_tp)//2
print(food_stuff_tp[middle])

first_three = food_stuff_tp[0:3]
last_three = food_stuff_tp[-3:]

print(first_three)
print(last_three)

del food_stuff_tp
food_stuff_tp = ('Apple', 'Orange', 'Banana', 'Grape', 'Mango', 'Potato', 'Tomato', 'Onion', 'Spinach', 'Garlic', 'Meat', 'Milk')

does_exist = "Onion" in food_stuff_tp

print(does_exist)


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

does_exist = 'Estonia' in nordic_countries 
exist = 'Iceland'  in nordic_countries
print(does_exist)
print(exist)




