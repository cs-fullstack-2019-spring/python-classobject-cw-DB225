def main():
    #problem1()
    #problem2()
    #problem3()
    #problem4()
    #challenge()

#PROBLEM1
#Create a class Dog.
#Make sure it has the attributes name, breed, color, gender.
#Create a function that will print all attributes of the class.
#Create an object of Dog in your problem1 function and print all of it's attributes.
def problem1():
    class Dog:
        def __init__(self, name, breed, color, gender):
            self.name = name
            self.breed = breed
            self.color = color
            self.gender = gender

        def __str__(self):
            return (f"My dog's name is {self.name}, he is a {self.gender} {self.color} {self.breed} ")

    newDog = Dog("Roky","Rotweiler","black","male")
    print(newDog)

##################################################################################
#PROBLEM2
#Create a function that has a loop that quits with the equal sign.
#If the user doesn't enter the equal sign, ask them to input another string.
def problem2():
    userInput = ''
    while(userInput != "="):
        userInput = input("Put a string: ")

##################################################################################
#PROBLEM3
#In your main file create three Person objects.
# Change the weight and height of each one.
# Afterwards, print the BMI (body mass index) of each Person.
# If you don’t know how to calculate BMI, look at the code I provided for you.
#Hint: BMI is (weight / (height * height)) x 703. Weight is in pounds and height is in inches.
#Extra:Put the three person objects in an array and use a loop to print out their BMIs.
def problem3():
    class Person:
        def __init__(self,name,weight,height):
            self.name = name
            self.weight = weight
            self.height = height

        def __str__(self):
            return(f"{self.name}'s size is {self.height}IN and weigh {self.weight} lbs")

        def bmi(self,):
            bmi = (self.weight) / (self.height * self.height) * 703
            return bmi

    newPerson1 = Person("kenn", 5, 225)
    newPerson2 = Person("kevin", 6, 200)
    newPerson3 = Person("Erin", 5, 170)

    print(newPerson1)
    print(newPerson2)
    print(newPerson3)

    print(f"The BMI of kenn is {newPerson1.bmi()}")
    print(f"The BMI of kevinis {newPerson2.bmi()}")
    print(f"The BMI of Erin is {newPerson3.bmi()}")



##################################################################################
#PROBLEM4
#Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#The class should have changeProduct:
#a) If changeProduct has one parameter, it can change the name of the product.
#b) If changeProduct has two parameters it can change the name and price of the product.
#c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
#Create an object of Product in your problem4 function and print all of it's attributes.
def problem4():
    class Product:
        def __init__(self, name="", price='', quantity=''):
            self.name = name
            self.price = price
            self.quantity = quantity

        def changeProduct(self,newName,newPrice,newQuantity):
            self.name = newName
            self.price = newPrice
            self.quantity = newQuantity

        def __str__(self):
            return (f"{self.name} , {self.price}, {self.quantity}")

    newProduct1 = Product("Computer", 500, 10)
    newProduct2 = Product(500, 10)
    newProduct3 = Product(10)
    print(newProduct1)
    print(newProduct2)
    print(newProduct3)
##################################################################################
#CHALLENGE
#Use a standard JavaScript template. In your main function create the array below:
#var squad = ["Bob", "John", "Bob", "Kenn", "Bob", "Kevin", "John", "Kevin"];
# Print how many times each name is present in the array.
#def challenge():

    #squad = ["Bob", "John", "Bob", "Kenn", "Bob", "Kevin", "John", "Kevin"]
    #counter = 0





##################################################################################
if __name__ == '__main__':
    main()