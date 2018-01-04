# David Wertenteil
#
# pip install requests
import requests
import json

# Load facebook token from file
# You can find it here: https://developers.facebook.com/tools/explorer/
with open('token.txt', 'r') as t:
    token = t.read()


def comment_on_posts(posts, amount):
    counter = 0
    for post in posts:
        if counter >= amount:
            break
        else:
            counter = counter + 1
        url = "https://graph.facebook.com/{0}/comments".format(post['id'])
        message = "Hi bro!"
        parameters = {'access_token': token, 'message': message}
        s = requests.post(url, data=parameters)


def get_posts():
    payload = {'access_token': token}
    r = requests.get('https://www.facebook.com/groups/', params=payload)
    print(r)
    result = json.loads(r.text)
    return result['data']


if __name__ == "__main__":
    get_posts()
    # print(posts)
    comment_on_posts(posts, 25)