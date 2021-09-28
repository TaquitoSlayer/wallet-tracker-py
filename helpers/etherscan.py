import requests
import logging
from web3 import Web3
from decimal import Decimal

def get_balance(wallet, api_key='YourApiKeyToken'):
    query = f'https://api.etherscan.io/api?module=account&action=balance&address={wallet}&tag=latest&apikey={api_key}'
    resp = requests.get(query)

    try:
        balance = resp.json()['result']
        balance_ether = Web3.fromWei(Decimal(balance), 'ether')
        print('CURRENT BALANCE:', balance_ether)
    except Exception as e:
        logging.info(e)
        pass
