import requests

def get_eth():
    resp = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/spot')
    return resp.json()['data']['amount']
