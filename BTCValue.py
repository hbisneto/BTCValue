### API: https://api.coindesk.com/v1/bpi/currentprice.json
import requests

def Main():
    URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    Response = requests.get(URL)
    Data = Response.json()

    MyDict = {}

    MyDict['USD_Code'] = Data['bpi']['USD']["code"]
    MyDict['USD_Symbol'] = Data['bpi']['USD']["symbol"]
    MyDict['USD_Rate'] = Data['bpi']['USD']["rate"]
    MyDict['USD_Description'] = Data['bpi']['USD']["description"]
    MyDict['USD_RateFloat'] = Data['bpi']['USD']["rate_float"]

    MyDict['GBP_Code'] = Data['bpi']['GBP']["code"]
    MyDict['GBP_Symbol'] = Data['bpi']['GBP']["symbol"]
    MyDict['GBP_Rate'] = Data['bpi']['GBP']["rate"]
    MyDict['GBP_Description'] = Data['bpi']['GBP']["description"]
    MyDict['GBP_RateFloat'] = Data['bpi']['GBP']["rate_float"]

    MyDict['EUR'] = Data['bpi']['EUR']["code"]
    MyDict['EUR_Code'] = Data['bpi']['EUR']["code"]
    MyDict['EUR_Symbol'] = Data['bpi']['EUR']["symbol"]
    MyDict['EUR_Rate'] = Data['bpi']['EUR']["rate"]
    MyDict['EUR_Description'] = Data['bpi']['EUR']["description"]
    MyDict['EUR_RateFloat'] = Data['bpi']['EUR']["rate_float"]

##  MyDict['BRL_Code'] = Data['bpi']['BRL']["code"]
##  MyDict['BRL_Symbol'] = Data['bpi']['BRL']["symbol"]
##  MyDict['BRL_Rate'] = Data['bpi']['BRL']["rate"]
##  MyDict['BRL_Description'] = Data['bpi']['BRL']["description"]
##  MyDict['BRL_RateFloat'] = Data['bpi']['BRL']["rate_float"]

    print("=" * 80)
    print(MyDict.get("USD_Code"))
    print(MyDict.get("USD_Symbol"))
    print("Valor do BTC em DOLLAR: " + MyDict.get("USD_Rate"))
    print(MyDict.get("USD_Description"))
    print("=" * 80)

    print("=" * 80)
    print(MyDict.get("GBP_Code"))
    print(MyDict.get("GBP_Symbol"))
    print("Valor do BTC em POUNDS: " + MyDict.get("GBP_Rate"))
    print(MyDict.get("GBP_Description"))
    print("=" * 80)

    print("=" * 80)
    print(MyDict.get("EUR_Code"))
    print(MyDict.get("EUR_Symbol"))
    print("Valor do BTC em EURO: " + MyDict.get("EUR_Rate"))
    print(MyDict.get("EUR_Description"))
    print("=" * 80)

##  print("=" * 80)
##  print(MyDict.get("BRL_Code"))
##  print(MyDict.get("BRL_Symbol"))
##  print("Valor do BTC em REAL: " + MyDict.get("BRL_Rate"))
##  print(MyDict.get("BRL_Description"))
##  print("=" * 80)
