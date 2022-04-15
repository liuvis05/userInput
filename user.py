#Exercise 2
name = input ("Please enter your full name: ")

#Split the name into first and last
#Capitalized the first letter
fullName = name.split()
nameTitle = name.title()
print(nameTitle)


nameSplit = nameTitle.split()
firstName =nameSplit[0]
lastName =nameSplit[1]

#Parse the age info to an int
age = input("Enter you age : ")
age = int(age)
#print (age)


#Record the employee's birth year
birthday=input("What is your B'day? (in MM/DD/YYYY) ") 
#print(str(birthday)[-4:])

#Concatenate the first and last name with a "."
#print(fullName[0] +"."+fullName[1])

#Add the last two digits of their birth year to the last name 
birthYear = (str(birthday)[-2:])
print("Your username is: " + fullName[1] + str(birthday)[-2:])

#Add @company.com to the end
print("Your email address is " + fullName[0] + "." + fullName[1] + birthYear + "@company.com")
