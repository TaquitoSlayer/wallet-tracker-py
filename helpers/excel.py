import pandas as pd
# unused import but used to gen requirements.txt
import openpyxl

def update_balance(balance=0, time=0, usd_balance=0):
    path = './../balance.xlsx'
    df1 = pd.DataFrame({
        'Time': ['Timetest12314'],
        'Balance': [1.88112],
        'USD': ['100007344']
        })
    df2 = pd.read_excel(path, sheet_name='wallet_tracking')
    res = pd.concat([df2, df1])
    writer = pd.ExcelWriter(path, engine='openpyxl', mode='a', if_sheet_exists='replace')
    res.to_excel(writer, sheet_name='wallet_tracking', index=False)
    writer.save()
