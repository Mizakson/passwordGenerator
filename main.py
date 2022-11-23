import secrets  # used to create secure and random strings of nums and special chars
import string   # used to import letters of the alphabet

alphabet = string.ascii_letters + string.digits  # defining 'alphabet' as all nums and letters
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))  # made num of chars 10
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)  # at least 3 uppercase chars
            and sum(c.isdigit() for c in password) >= 3):  # at least 3 digits
        break

print(f'Here is your random password! {password}')
