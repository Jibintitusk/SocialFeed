import requests
#import facebook
from configure import *
ppid="109302414885699_110756948073579"
url="https://graph.facebook.com/{ppid}?access_token={page_token}"
response=requests.delete(url.format(ppid=ppid,page_token=page_token))
print(response._content),200


