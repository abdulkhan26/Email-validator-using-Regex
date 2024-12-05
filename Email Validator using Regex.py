import re

pattern="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email=input("Enter your Email:")

if re.search(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")