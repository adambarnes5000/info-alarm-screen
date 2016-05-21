import urllib2
import random
import json

null=None
true=True
false=False


def split_text(text):
    lines = []
    line = ''
    words = text.split(" ")
    for word in words:
        if len(line)+len(word)<21:
            line = line + ' ' + word
        else:
            lines.append(line)
            line=word
    lines.append(line)
    return lines


def get_no_context():
    return split_text(random.choice(get_posts()))


def get_posts():
    hdr = {'User-Agent': 'no context bot'}
    req = urllib2.Request(
        "https://www.reddit.com/r/quotes/top.json?sort=top&t=week",headers=hdr)
    data = json.loads(urllib2.urlopen(req).read())
    children = data['data']['children']
    return map(lambda x:x['data']['title'].replace('\'',"").replace('-','').replace('"','').replace("'",''),children)


print get_no_context()
