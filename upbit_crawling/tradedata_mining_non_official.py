import requests
import pandas as pd
from time import sleep

def call_coin():
    #coin 종류 가져오기
    databox=[]
    url = 'https://api.upbit.com/v1/market/all'
    response = requests.get(url)
    datas = response.json()
    # 데이터 프레임으로 변경
    df = pd.DataFrame(datas)
    # market 기준 한화로 변경
    coins_krw = df[df['market'].str.startswith('KRW')].reset_index(drop=True)
    num_index = len(coins_krw.index)
    for i in range(0, num_index):
        empty = [coins_krw.iloc[i,0],coins_krw.iloc[i,2]]
        databox.append(empty)
    return databox

# months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']


coin_names=call_coin()
# cycle=0
for coin in coin_names:
    box = {}

    r = requests.get("https://crix-api-endpoint.upbit.com/v1/crix/candles/days?code=CRIX.UPBIT."+coin[0]+"&count=90&to=2021-03-31%2009:00:00")
    tradedata = r.json()

    for trade in reversed(tradedata):
        time = trade['candleDateTime']
        timedata = time[0:10]
        op = trade['openingPrice']  # op 는 시작 가격
        tp = trade['tradePrice']  # tp 는 종가
        lp = trade['lowPrice']  # lp 는 저가
        hp = trade['highPrice']  # hp 는 고가
        volume=trade['candleAccTradeVolume']
        price=trade['candleAccTradePrice']
        tap=price/volume
        box[timedata] = [op,hp,lp,tp,volume,price,tap]

    tradedata = pd.DataFrame(box)
    tradedata.rename(index={0: "Open Price", 1: "High Price", 2: "Low Price", 3: 'Close Price',4:'Trade Volume',5:'Total trade-price',6:'Average Trade price'}, inplace=True)
    transposed_tradedata = tradedata.transpose()
    transposed_tradedata.to_excel(excel_writer='C:/Users/whdtlr/Bitcoin_desktop/2021/'+coin[1]+'.xlsx')
    print(coin[1])
    # cycle+=1
    # if cycle%5==0:
    #     sleep(60)
    #     print("-------waiting-------")
