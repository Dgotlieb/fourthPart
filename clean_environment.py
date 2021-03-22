import requests

def rm_test_user(id):
    # Delete test user from the automation
    try:
        requests.delete('http://localhost:5002/users/%s' % id)
        print(" post delete user action")
    except requests.exceptions.ConnectionError as e:
        print("Connection refused to rest_app service", e)


def rm_specific_user(id):
    # Delete specific user from the automation
    try:
        requests.delete('http://localhost:5002/users/%s' % id)
        print("user %s" % id + " has been deleted")
    except requests.exceptions.ConnectionError as e:
        print("Connection refused to rest_app service", e)


def stop_rest_app():
    # Stop rest app service
    try:
        requests.get('http://localhost:5002/stop_server')
    except requests.exceptions.ConnectionError as e:
        print("Connection refused to rest_app service", e)


if __name__ == "__main__":
    rm_test_user('1')
    stop_rest_app()

