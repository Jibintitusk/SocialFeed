import requests
from configure import *
ppid='109302414885699_110288854787055'
msg=input('Enter comment')
url="https://graph.facebook.com/{ppid}/comments?message={msg}&access_token={page_token}"
res=requests.post(url.format(ppid=ppid,msg=msg,page_token=page_token))
print(res._content)
