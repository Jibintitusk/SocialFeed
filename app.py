import facebook
import requests
from configure import *
class Facebook:
    def __init__(self,msg) :
        self.msg=msg
    def post(self):
        msg=self.msg
        url="https://graph.facebook.com/{page_id}/feed?message={msg} !&access_token={page_token}"
        res=requests.post(url.format(page_id=page_id,msg=msg,page_token=page_token))
        print(res._content)
    def get(self):
        url="https://graph.facebook.com/{page_id}/feed?access_token={page_token}"
        res=requests.get(url.format(page_id=page_id,page_token=page_token))
        print(res._content)
msg=input('Enter the Caption')
s=Facebook(msg)
s.post()