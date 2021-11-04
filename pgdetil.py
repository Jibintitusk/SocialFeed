import requests
from configure import *
url="https://graph.facebook.com/{page_id}?fields=about,name,attire,bio,location,parking,hours,emails,website&access_token={page_token}"
res=requests.get(url.format(page_id=page_id,page_token=page_token))
print(res._content)