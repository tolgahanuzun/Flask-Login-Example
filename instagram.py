"""View Instagram user follower count from Instagram public api"""
import requests


def get_followed_by(username):
    """View Instagram user follower count"""
    link = f"https://www.instagram.com/{username}/?__a=1&__d=1"
    user = requests.get(link)
    return (user.json()['graphql']['user']['edge_followed_by']['count'])


def get_user_name(url):
    """Split the URL from the username"""
    username = url
    if url.find("instagram.com") >= 0:
        username =  url.split("instagram.com/")[1].replace("/", "")
    return username