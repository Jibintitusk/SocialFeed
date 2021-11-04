import requests
from configure import *
url="https://graph.facebook.com/{user_id}/accounts?access_token={user_token}"
res=requests.get(url.format(user_id=user_id,user_token=user_token))
print(res.content)