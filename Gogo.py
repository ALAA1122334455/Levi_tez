import random,httpx
from threading import Thread
num=0
def gets():
    num = '56789'
    user = 'qwertyuiopasdfghjkl_zxcv1234567890_bnm'

    rng = int("".join(random.choice(num) for i in range(1)))

    name= str("".join(random.choice(user) for i in range(rng)))
    return name
def checkg(uso):
    a = httpx.get(f"https://gmail-mhros-e438ac1b0be7.herokuapp.com/qredes/gmail/?email={uso}")
    if '"status":"good"' in a.text:
        return True
    else:return False
def cheki():
  try:
    global num
    uso=gets()
    
    cc = httpx.get(f'https://api-zi-7c2fc6a6a5b2.herokuapp.com/api/instagram/zaid.k.k/v2.z.k/v1/{uso}').text
    if 'OK' in cc:
        po=checkg(uso)
        if po==True:
            num+=1
            print(uso,num)
            httpx.get(f"https://api.telegram.org/bot5870224472:AAGuBQtXvCE9xg83EuLGL_yzagKXkqwdhcM/sendMessage?chat_id=749219602&text={uso}")
        else:print('شغال',po);pass
    else:pass
  except:pass
while True:
    threads = []
    for i in range(77):
        thread = Thread(target=cheki)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
