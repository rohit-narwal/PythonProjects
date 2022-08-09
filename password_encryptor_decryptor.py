from cryptography.fernet import Fernet
from Password_generator import password_maker
password = password_maker(5)

key = Fernet.generate_key()

fernet = Fernet(key)

encPassword = fernet.encrypt(password.encode())
decPassword = fernet.decrypt(encPassword).decode()
print("The encoded password is :",encPassword)
print("The decoded password is :",decPassword)