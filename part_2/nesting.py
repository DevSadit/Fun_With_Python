# nesting in conditional

user_name = input("user name: ")
user_pass = int(input("password: "))

if user_name == "admin" and user_pass == 00:
    print("loged in succesfully!")

else:
    if user_name != "admin":
        print("wrong user name!")
    else:
        print("wrong password, try again")
