from helpers import etherscan
from helpers import excel
from helpers import coingecko
import json
import random
import time

wallet = json.load(open("./configs/wallet.json", "r"))
# lazy coding here
time_sleep = wallet['time_interval']
wallet = wallet['wallet']

keys = json.load(open("./configs/api_keys.json", "r"))['keys']['etherscan']

def main():
    try:
        balance_ether = etherscan.get_balance(wallet, random.choice(keys))
        eth_usd = coingecko.get_eth()
        balance_usd = float(balance_ether) * float(eth_usd)
        excel.update_balance(balance_ether, balance_usd)
    except Exception as e:
        print(e)
        pass

while True:
    print('WRITING TO XLSX')
    main()
    print('DONE')
    minutes = time_sleep / 60
    print(F'CHECKING IN THE NEXT {minutes} MINUTES')
    time.sleep(time_sleep)
