import random
import string

def generate_password(length):
    """Generate a random password of fixed length """
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

passlen = int(input("Enter the length of password: "))
p = generate_password(passlen)
print(p)