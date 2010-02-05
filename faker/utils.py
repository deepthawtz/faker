import random

__rand = lambda x: random.choice(x.split())
__numerify = lambda x: re.sub("#", random.randint(9), x)
__letterify = lambda x: re.sub("\?", __rand([chr(i) for i in range(ord('A'), ord('Z')+1)], x))
__bothify = lambda x: __letterify(__numerify(x))
