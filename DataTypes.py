#This is List (Ordered, can't be changed and duplicate is present)
#Square bracket
fruits = ["apple","banana",1,2,3]

print (fruits)
print(fruits[2:-1])

#You can update value from list
fruits[1] = "grapes"
print(fruits)

#You can add value in the list using "append"
fruits.append(10)
print(fruits)

#You can add value using index with the help of "insert"
#Note: Specify the index where you want to insert then value to be insert
fruits.insert(2,40)
print(fruits)
#End of List



#This is Dictionary (Unordered, can be changed and Duplicate is not present)
#Curly bracket
#Note: Value of the keys can be duplicate

courses = { 1: 'Python',
            2: 'AI Technology',
            'Third': 'Big Data'}

print(courses)
print(courses.get('Third'))

#You can change value using index in dictionary
courses['Third'] = 'Data Scientist'
print(courses)


#You can add in dictionary
courses[4] = 'Big Data'
print(courses)
#End of Dictionary




#This is Tuple (Ordered, cannot be changed and Duplicate is present)
#Parenthesis
#You can use index value
animals = ('lion','zebra','snake',10,10,20,30)
print(animals)

#Using Index Value
print(animals[3])

#You can count the number of duplicate value inside
print(animals.count(10))
#End of Tuple


#This is Set (Unordered and Duplicate is not present)
#Curly Bracket
#Set does not support indexing

myself = {10,10,10,20,20,30,"course"}
print(myself)
#End of Set


#Range and list
print(list(range(11)))


#List and Dictionary Combine
combination = [fruits , courses]
print(combination)

