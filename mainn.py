from flask import Flask, jsonify
import http.client
import json

app = Flask(__name__)

@app.route('/get_proxy')
def get_google_proxy():
    conn = http.client.HTTPSConnection("gimmeproxy.com")
    conn.request("GET", "/api/getProxy?websites=google")
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_data = json.loads(data)
    conn.close()
    return jsonify({json_data['protocol']: json_data['curl']})

app.run()
