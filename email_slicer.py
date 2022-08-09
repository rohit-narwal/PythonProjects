import re

# Make a regular expression
# for validating an Email
email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# getting the email input from user
# def email_getter():
#     # while True:
#     email = input("Enter the gmail: ")
#         # if "@" in email and "." in email:
#         #     break
#         # else:
#         #     print("Enter email only")
#         #     continue
#     return email

# Define a function for
# for validating an Email
def check():
    # pass the regular expression
    # and the string into the fullmatch() method
    while True:
        email = input("Enter the gmail: ")  # email_getter()
        if(re.fullmatch(email_format, email)):
            print("Email correct")
            break
        else:
            print("Email format wrong")
            continue
    return email

## verifying the email format
## algorithm to find @ and . inside email and check if @ comes first
## to match email format
# def verifier():
#     while True:
#         email = email_getter()
#         at_rate = 0
#         dot = 0
#         length = len(email)
#         for i in range(length):
#             if email[i] == "@":
#                 at_rate = i
#             elif email[i] == ".":
#                 dot = i
#         if "@" in email and "." in email and at_rate<dot:
#             break
#         else:
#             continue
#     return email
# check(email_getter())
# making a class

class email_slice:
    def __init__(rohit, email):
        rohit.email = email
    # getting username
    def user_name_get(self):
        user_name = self.email.split("@")[0]
        return user_name
    # getting the domain
    def domain_get(self):
        domain = self.email.split("@")[1]
        return domain
    # printing the username and domain
    def result(self):
        return "Username is: "+ \
        self.user_name_get() + \
        "\nDomain is: "+self.domain_get()

obj = email_slice(check())
print(obj.result())