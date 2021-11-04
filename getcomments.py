import requests
#import facebook
from configure import *
ppid="109302414885699_110125801470027" #page-post-id
url="https://graph.facebook.com/{ppid}/comments?access_token={page_token}"
response=requests.get(url.format(ppid=ppid,page_token=page_token))
print(response._content)