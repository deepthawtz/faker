import re
import random

_rand = lambda x: random.choice(x.split())
_numerify = lambda x: "".join([re.sub("#", str(random.randint(0,9)), i) for i in x])
_letterify = lambda x: "".join([re.sub(r"\?", random.choice([chr(i) for i in range(ord('A'), ord('Z')+1)]), y) for y in x])
_bothify = lambda x: _letterify(_numerify(x))
