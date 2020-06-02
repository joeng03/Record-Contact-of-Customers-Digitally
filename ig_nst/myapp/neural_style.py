import requests

def get_image(content_url,style_url):
    r = requests.post("https://api.deepai.org/api/fast-style-transfer",
    files={
        'content':content_url,
        'style':style_url
    },
    headers={'api-key': '62825b8a-790e-4348-8f23-5f51ce159871'})
    return r.json()