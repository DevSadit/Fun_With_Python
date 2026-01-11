# logical operations in expressions
age = int(input("provide a age: "))

if age <= 14:
    print("child")
elif age >= 14 and age < 18:
    print("you are a tenager!")

else:
    print("you are an adult")
