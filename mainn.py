from flask import Flask, jsonify
from flask import request
import os
import random
from secrets import token_hex
from user_agent import generate_user_agent

import httpx

app = Flask(__name__)

def FromCreate(email):
    try:
        csr = token_hex(8) * 2
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/signup/email/',
            'user-agent': generate_user_agent('android'),
            'x-csrftoken': csr
        }

        data = {
            'email': email,
        }

        
        rrs = httpx.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data,proxies={'http': os.environ.get('PROXIMO_URL', '')})
        aj = str(rrs.text)
        print(aj)
        if 'few' in aj:
            return {'bad':'band'}
        elif 'taken' in aj:
            return {'status': 'available', 'dev': '3laa'}
        else:
            return {'status': 'unavailable', 'dev': '3laa'}
    except Exception as e:
        try:return FromCreate(email)
        except:return {'status': 'error', 'message': 'An error occurred'}

@app.route('/check_email/<email>')
def check_email(email):
    result = FromCreate(email)
    return jsonify(result)
if __name__ == '__main__':
    app.run(port='8080')
