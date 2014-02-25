import re
import random

from faker import data



rand = lambda x: random.choice(x.split())
numerify = lambda x: "".join([re.sub(r"#", str(random.randint(0,9)), i) for i in x])
letterify = lambda x: "".join([re.sub(r"\?", random.choice([chr(i) for i in range(ord('A'), ord('Z')+1)]), y) for y in x])
bothify = lambda x: letterify(numerify(x))

def domain():
    return rand(data.FREE_EMAIL)

def secondary_address():
    return numerify(random.choice(["Apt. ###", "Suite ###", ""]))

def uk_postcode():
    return bothify(random.choice(["??# #??","??## #??"]))

