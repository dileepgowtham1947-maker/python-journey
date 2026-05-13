# Day 4  : 30 Days of python programming  , start = 10:48 | End = 12:47 am

Exercises: Level 1

Declare an empty list

Declare a list with more than 5 items

Find the length of your list

Get the first item, the middle item and the last item of the list

Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#;  '

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list

Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.



  
## MY CODE FOR EXERCISE 1 PROBLEMS
# Day 4  : 30 Days of python programming 


  

empty = []
list = ["Dileep", "Gowtham", "Anything", 5.8, 2005, "Arya"]
print(len(list))

first = list[0]
second =list[2]
last = list[-1]
print(first, second, last)

mixed_data_types = ["Dileep", 20, 5.8, "Unmarried", "Anantapur" ]
it_companies = ["Facebook", "Google", "IBM", "Amazon", "Microsoft", "Apple", "Oracle"]
print(mixed_data_types)
print(len(mixed_data_types))

it_companies[0] = "Alphabet"
it_companies.append("HP")
print(it_companies)

it_companies.insert(3, "Laptap")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

it_companies = "#" . join(it_companies)
print(it_companies)

deos_exist = "Apple" in it_companies
print(deos_exist)

result = sorted(it_companies)
print(result)

it_companies = ["Facebook", "Google", "IBM", "Amazon", "Microsoft", "Apple", "Oracle"]
print(it_companies.sort(reverse=True))
print(it_companies)

first3 = it_companies[0:3]
print(first3)
last3 = it_companies[-3:]
print(last3)
middle = it_companies[3]
print(middle)

remove = it_companies.pop()
print(remove)

it_companies.clear()
print(it_companies)

del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
result = front_end + back_end
print(result)

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(4,"Python")
print(full_stack)
full_stack.insert(5,"SQL")
print(full_stack)
 



##Exercises: Level 2



The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
Find the middle country(ies) in the countries list
Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.



## MY CODE FOR EXERCISE 2 PROBLEMS
# Day 4  : 30 Days of python programming

