import requests,instaloader,os,httpx
from time import time
from hashlib import md5
from user_agent import generate_user_agent
from random import randrange
from threading import Thread
ids=[]
opi,opi1=0,0
def get_id():
  id=str(randrange(10070, 30975110))
  if id not in ids:
    ids.append(id)
    return id
  else:
    get_id()
def get_username():
  while True:
    try:
      global opi,opi1
      id=get_id()
      csrftoken = md5(str(time()).encode()).hexdigest()
      headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'dpr': '0.8',
    'origin': 'https://www.instagram.com',
    'user-agent': generate_user_agent(),
    'x-csrftoken': csrftoken,
    }
      data = {
    '__spin_b': 'trunk',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+id+'","username":"0s9s"}',
    'server_timestamps': 'true',
    'doc_id': '7666785636679494',
}
      response = httpx.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
      username=response['data']['user']['username']
      opi1+=1
      print(username,'from:',opi1)
      with open('3laa-availble2011.txt', 'a') as f:
                      f.write(username + '\n')
                      f.close()
    except Exception as e:

      pass
threads = []

for _ in range(97):
    thread =Thread(target=get_username)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()