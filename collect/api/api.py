# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = "EAACEdEose0cBAMqjagSZBoe7s9akBG2vZB3gWkb0w9GZCRdrCOu22BkLkRl4OMos1XUHwbR8F9lh3ViEzZBqErHQ9wFZCZBr0WQ46OctEUJ90uvyTTO2RJ5mABNImmltd8QOryhhN7GSUfFK2lZAeEylIJhZAOZBGiYNuOYXxmQdpJUiXvwNCT7heZAvIMkyrYtyX0lnBCTh0MJr1DTu5DlHiO2zuW3CqgaSUZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"
def fb_gen_url(
        base=BASE_URL_FB_API,
        node='',
        **params):
    url = '%s/%s/?%s' % (base,node, urlencode(params));
    return url

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(node=fb_name_to_id(pagename)+"/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since,
                     until=until,
                     limit=50,
                     access_token=ACCESS_TOKEN)

    # results = []
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        # results.append(posts)
        # results += posts

        url = None if paging is None else paging.get("next")
        isnext = url is not None

        yield posts





