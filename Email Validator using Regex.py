import re

pattern="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# ^ is used to start the regular expression and $ to end it
#[a-z] starting of the email address should be lower case and only alphabets from a to z
# [\._]? matches zero or one occurences of either a dot or an underscore
# [@] matches the @ symbol
# Matches one or more word characters, which include letters (a-zA-Z), digits (0-9), and underscores (_).
#T his part ensures that the domain extension has between 2 to 3 characters, such as .com, .org, or .net
email=input("Enter your Email:")

if re.search(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")
