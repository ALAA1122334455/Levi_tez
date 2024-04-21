from flask import Flask, request, jsonify
import random
import requests
import uuid
import string
from OneClick import *

app = Flask(__name__)
Hunter = Hunter

@app.route('/get_reset/<user>/<domain>', methods=['GET'])
def get_reset(user, domain):
    hd = str(Hunter.Services())
    
    head2 = {
        "user-agent": f"{hd}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; en_GB;)"
    }
    
    data = {
        "user_email": user,
        "guid": uuid.uuid4(),
        "device_id": "android-" + str(uuid.uuid4())
    }
    
    req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head2, data=data)
    
    if '"status":"ok"' in req.text:
        reset = req.json()['obfuscated_email']
        if not reset or not reset.endswith('@' + domain):
            return jsonify({'error': 'domain'}), 400
        first_char_user = user[0].lower()
        last_char_user = user[-1].lower()
        first_char_reset = reset.split('*')[0].lower()
        last_char_before_at = reset.split('@')[0][-1].lower()
        if first_char_reset == first_char_user and last_char_before_at == last_char_user:
            return jsonify({'reset': True, 'email': reset, 'dev': '3laa'})
        else:
            return jsonify({'reset': False, 'dev': '3laa'})
    elif 'Page Not Found' in req.text:
        reset = 'h**$@gmail.com'
        if not reset or not reset.endswith('@' + domain):
            return jsonify({'error': 'domain'}), 400
        return jsonify({'reset': False, 'email': reset, 'dev': '3laa'})
    else:
        reset = 'h**$@gmail.com'
        if not reset or not reset.endswith('@' + domain):
            return jsonify({'error': 'domain'}), 400
        return jsonify({'reset': 'banned or error', 'dev': '3laa'})
if __name__=='__main__':
  app.run()
