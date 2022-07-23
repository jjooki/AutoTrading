import jwt
import hashlib
import os
import pyupbit
import requests
import uuid
from urllib.parse import urlencode, unquote

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

def make_queryhash(params):
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")
    m = hashlib.sha512()
    m.update(query_string)
    return m.hexdigest()

def make_payload(query_hash = "a"):
    if query_hash == "a":
        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
        }
    else:
        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }
    return payload

def make_header(payload):
    jwt_token = jwt.encode(payload, secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    return {'Authorization': authorization,}

def account():
    payload = make_payload()
    
    jwt_token = jwt.encode(payload, secret_key).decode('utf8')
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
        'Authorization': authorization,
    }
    
    res = requests.get(server_url + '/v1/accounts', headers=headers)
    return res.json()

def market_info(ticker):
    if isinstance(ticker, str):
        params = {
            'market': ticker
        }
    else:
        return "Input string only!"

    query_hash = make_queryhash(params=params)
    payload = make_payload(query_hash=query_hash)
    headers = make_header(payload=payload)

    res = requests.get(server_url + '/v1/orders/chance', params=params, headers=headers)
    return res.json()

def order(ticker, side, ord_type, price, volume):
    if isinstance(ticker, str):
        params = {
            'market': ticker,
            'side': side,
            'ord_type': ord_type,
            'price': str(price),
            'volume': str(volume),
        }
    else:
        return "Input string only!"

    query_hash = make_queryhash(params=params)
    payload = make_payload(query_hash=query_hash)
    headers = make_header(payload=payload)

    res = requests.post(server_url + '/v1/orders', params=params, headers=headers)
    return res.json()
