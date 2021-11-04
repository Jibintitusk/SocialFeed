import requests
from configure import *
img="https%3A%2F%2F4.img-dpreview.com%2Ffiles%2Fp%2FE~TS590x0~articles%2F3925134721%2F0266554465.jpeg&imgrefurl=https%3A%2F%2Fwww.dpreview.com%2Fsamples%2F3925134721%2Ffujifilm-x-a3-sample-gallery&tbnid=zsxWnq3vNVEB7M&vet=12ahUKEwjylIbG2fbzAhXSktgFHQdWC8QQMygDegUIARDQAQ..i&docid=CvgrVEnJX5o2_M&w=590&h=393&q=sample%20images&ved=2ahUKEwjylIbG2fbzAhXSktgFHQdWC8QQMygDegUIARDQAQ"
url="https://graph.facebook.com/{page_id}/photos?url={img}&access_token={page_token}"
res=requests.post(url.format(page_id=page_id,img=img,page_token=page_token))
print(res._content)
