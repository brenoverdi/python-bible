##Asking user for a name

userName = input("Hello there! Welcome to 'Hello you', please type your full name: ")
age = input("Please, type you age: ")
city = input("Now, please type your city: ")
hobbies = input("Now, please, type what are your hobbies: ")

print("Name: " + userName, "\nAge: " + age, "\nCity: " + city, "\nHobbies: " + hobbies)

confirming_info = "Your name is {}, you are {} years old, you live in {} and your hobbies are: {}"
confirming_info = confirming_info.format(userName, age, city, hobbies)
print(confirming_info)

confirm_option = input("Is the information above correct? Type yes or no: ")
if confirm_option == "yes":
    print("Thank you for participating!")
else:
    print("Sorry, you must fill your answers again")
