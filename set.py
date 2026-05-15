## Day 6  : 30 Days of python programming

## Exercises: Level 1


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard



## MY CODE FOR ALL PROBLEMS


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["AWS", "HP", "Cognizant", "JPMorgan"])
print(it_companies)

it_companies.remove("Facebook")
print(it_companies)



## Exercises: Level 2


Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely


## MY CODE FOR ALL PROBLEMS


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B))

A.intersection(B)
print(A)

print(A.issubset(B))
print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

del A
del B



## Exercises: Level 3


Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.


  
## MY CODE FOR ALL PROBLEMS  

sentance = "I am a teacher and I love to inspire and teach people"  

words = sentance.split()
unq_words = set(words)
print(unq_words)

print(len(unq_words))





