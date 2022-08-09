import random
import string

words=string.ascii_letters+string.digits+"!@#$%^&*()"

length = int(input("Enter the length for password: "))

def password_maker(length):
    password_words = []
    for i in range(length):
        password_words.append
        (
            random.choice(words)
        )
    password = "".join(password_words)
    return password

if __name__ == "__main__":
   obj = password_maker(length)
   print("The password is :", obj)



## or

# password_words = random.sample(words, length)

# print("Your password is:", "".join(password_words))