pass1 = input("enter your password")
pass2 = input("confirm your password")

if pass1 == pass2:
    print("password is matching")
else:
    if pass1.casefold() == pass2.casefold():
        print("please check for the cases and try again")
    else:
        print("np they are not matching try them again")


