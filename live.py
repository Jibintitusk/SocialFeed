import requests
from configure import *
u="https://graph.facebook.com/{user_id}/live_videos?status=LIVE_NOW&title=Today%27s%20Live%20Video&description=This%20is%20the%20live%20video%20for%20today.&access_token={user_token}"
#url="https://graph.facebook.com/v3.3/me/live_videos?status=LIVE_NOW&access_token={user_token}"
res=requests.post(u.format(user_id=user_id,user_token=user_token))
print(res._content)