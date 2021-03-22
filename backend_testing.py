import requests
import db_connector

def usrPost():
    res = requests.post('http://localhost:5002/users/1', json={"user_name":"John"})
    if res.ok:
        print(res.json())
    else:
        print(res.json())
    print(' Database AFTER POST query found user_name: ' + db_connector.get_user_name(1) + ' For user_id: 1')

def usrGet():
    res = requests.get('http://localhost:5002/users/1')
    if res.ok:
        print(res.json())
    else:
        print(res.status_code)
        print(res.json())
    print(' Database AFTER GET query found user_name: ' + db_connector.get_user_name(1) + ' For user_id: 1')

def usrPut():
    res = requests.put('http://localhost:5002/users/1', json={"user_name":"John-updated"})
    if res.ok:
        print(res.json())
    else:
        print(res.status_code)
        print(res.json())
    print(' Database AFTER PUT query found user_name: ' + db_connector.get_user_name(1) + ' For user_id: 1')

def usrDel():
    res = requests.delete('http://localhost:5002/users/1')
    if res.ok:
        print(res.json())
    else:
        print(res.status_code)
        print(res.json())
    print(' Database AFTER DELETE query found user_name: ' + db_connector.get_user_name(1) + ' For user_id: 1')


if __name__ == '__main__':
    usrPost()
    usrGet()
    usrPut()
    usrDel()
