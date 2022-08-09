from Password_generator import password_maker

length = int(input("Enter the length of password: "))
password = password_maker(length)

algorithm_pattern = {
    "a":"1", "b":"?", "c":"g", "d":"5", "e":"y", "f":"j", "g":"0",
    "h":"6", "i":"q", "j":"e", "k":"w", "l":"^", "m":"*", "n":"#",
    "s":"7", "t":"9", "u":"1", "v":"%", "w":")", "x":"(", "y":";",
    "z":":", "1":">", "2":"<", "3":".", "4":"?", "5":"y", "6":"9",
    "7":"L", "8":"D", "9":"Y", "0":"Q"
}
print("The before any changes: ",password)

encPassword = password[::-1]
print("Password Before Algorithm:", encPassword)
for word, enc_form in algorithm_pattern.items():
    for i in range(len(password)):
        if(password[i]==word):
            encPassword = encPassword.replace(word,
            algorithm_pattern[word])
print("Password after Algorithm:",str(encPassword))