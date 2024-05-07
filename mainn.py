import httpx
import requests
import random
import threading
import time
from user_agent import generate_user_agent
from uuid import uuid4
from secrets import token_hex
nums=0
def gtpr():
      
      dataa=httpx.get('https://gimmeproxy.com/api/getProxy?get=true&post=true&supportsHttps=true&anonymityLevel=1&cookies=true&referer=true&user-agent=true').json()
      dato=dataa["curl"]
      proX={'http://':f'{dato}','https://':f'{dato}'}
      return proX,dataa
      
def check(email):
        global nums
        memo = random.randint(100, 300)
        O = f'\x1b[38;5;{memo}m'
        csr = token_hex(8) * 2
        uid = uuid4().hex.upper()
        miid = token_hex(13).upper()
        dtr = token_hex(13)

        cookies = {
            'csrftoken': csr,
            'dpr': '2.1988937854766846',
            'ps_n': '0',
            'ps_l': '0',
            'mid': miid,
            'ig_did': uid,
            'datr': dtr,
            'ig_nrcb': '1',
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '2.19889',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'viewport-width': '891',
            'x-asbd-id': '129477',
            'x-csrftoken': csr,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1012280089',
            'x-requested-with': 'XMLHttpRequest',
        }

        timestamp = str(time.time()).split('.')[0]
        data = {
           'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:mahos999',
            'email': email,
            'first_name': 'Ahmedalhrrani',
            'username': "dtgcyc75chuc",
            'client_id': miid,
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'false',
        }
        getsp=gtpr()
        proxe=getsp[0]
        datap=getsp[1]
        res = httpx.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=proxe
        ).text
        if 'الخطأ' in res:pass
        else:nums+=1;print(res,nums)
def chg():
 while True:
  try:check('ronaldo@gmail.com')
  except:pass
Threads = []
for _ in range(30):
    t = threading.Thread(target=chg)
    t.start()
    Threads.append(t)

for thread in Threads:
    thread.join()
