import random
import string


pass_len=12
charVal = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charVal)

print(f"Your random password is: {password}")


#Second Methode
#list comprehension (function for i in range(n))

res = "".join([random.choice(charVal) for i in range (pass_len)])
print(res)
