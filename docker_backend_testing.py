import requests

def testbe():
    res = requests.get('http://localhost:5004/users/1')
    if res.ok:
        print(res.json())
    else:
        print(res.status_code)
        print(res.json())

testbe()
