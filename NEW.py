import secrets
import string

stringSource  = string.ascii_letters + string.digits + string.punctuation
password = secrets.choice(string.ascii_lowercase)
password += secrets.choice(string.ascii_uppercase)
password += secrets.choice(string.digits)
password += secrets.choice(string.punctuation)

for i in range(6):
    password += secrets.choice(stringSource)

char_list = list(password)
secrets.SystemRandom().shuffle(char_list)
password = ''.join(char_list)
print ("Secure Password is ", password)

print ("Reset password URL Link")
SecureURL = "https://pynative.com/user/jhon/reset="
SecureURL+=secrets.token_urlsafe(32)

print(SecureURL)