# What is this?
This is a small script that you can use with pm2 or whatever process manager you like to track your earnings in your Ethereum wallet. This can be synced up with Google Drive giving you access to your earnings anywhere at anytime. This can be ran on a server or locally on your own computer by installing python 3+ and running pip to install requirements.txt

The result:<br />
![](https://pbs.twimg.com/media/FAfGvaJUcAALNN6?format=png&name=small)

# How to use?
First, install [python3 on your system](https://docs.python-guide.org/).<br />
For non-windows users, install [pip3](https://raturi.in/blog/installing-python3-and-pip3-ubuntu-mac-and-windows/) like so. Windows users, just select it in the installer before clicking install.<br />

Once you have that done, open your command line and navigate to your folder that you've downloaded this in and run:<br />
```pip3 install -r requirements.txt```<br />

Go into wallet.json in the configs folder and edit the time_interval to something you would prefer. Change the wallet to yours as well.<br />
e.g. 60 would mean the script will update the xlsx sheet every 60 seconds.<br /><br />

After that, open a terminal/cmd in the directory that you downloaded this project and run main.py<br />
e.g. ```python main.py``` or
```python3 main.py```
<br />
You can edit everything but the wallet_tracking sheet.<br />

# Why?
The ETH/USD volatility and traders in futures, NFTs, or anything involving the change of your ETH balance being rapid requires some kind of tracking to see if you're at a loss or not. With the help of checking the change in ETH/USD, you can make your own conclusions on if you were up for the day. Of course, for bigger size wallets, this is kind of useless because of the basis of counting ETH vs USD and the debate of where crypto will go. This is for everyone else that wants to have tracking on the real $. You can create your own charts in other sheets besides wallet_tracking to help you visualize where you're at. Etherscan has something for this, but it's off by a day, and does not account for the USD change. You can also see the change on your phone or tablet while out for lunch, without having to sync up your wallet information to an app that you don't know where the data is stored.
