import requests
from configure import page_token
url="https://graph.facebook.com/pages/search?q=Facebook&fields=id,name,location,link&access_token={page_token}"
res=requests.get(url.format(page_token=page_token))
print