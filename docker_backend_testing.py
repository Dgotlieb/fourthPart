import requests

def testbe():
    res = requests.get('http://127.0.0.1:5000/users/1')
    if res.ok:
        print(res.json())
    else:
        print(res.status_code)
        print(res.json())