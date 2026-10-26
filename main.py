import secrets
import string

version = "1.0.0"


upper = True
lower = True
numbers = True
symbols = True
length = 10

pool = ""
if upper: pool += string.ascii_uppercase
if lower: pool += string.ascii_lowercase
if numbers: pool += string.digits
if symbols: pool += string.punctuation

pw = ""
for i in range(length):
    pw += secrets.choice(pool)

print(pw)