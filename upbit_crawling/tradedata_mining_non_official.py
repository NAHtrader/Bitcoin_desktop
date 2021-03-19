import requests
import pandas as pd
from fake_useragent import UserAgent
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

days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
hours = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

coin_names=[['KRW-PCI', 'PayCoin'], ['KRW-STRAX', 'Stratis'], ['KRW-AQT', 'Alpha Quark Token'], ['KRW-BCHA', 'Bitcoin Cash ABC'], ['KRW-GLM', 'Golem'], ['KRW-QTCON', 'Quiztok'], ['KRW-SSX', 'SOMESING'], ['KRW-META', 'Metadium'], ['KRW-OBSR', 'Observer'], ['KRW-FCT2', 'FirmaChain'], ['KRW-LBC', 'LBRY Credits'], ['KRW-CBK', 'Cobak Token'], ['KRW-SAND', 'The Sandbox'], ['KRW-HUM', 'Humanscape'], ['KRW-DOGE', 'Dogecoin']]
cycle=0
for coin in coin_names:
    box = {}
    for day in days:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        for hour in hours:
            r = requests.get("https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT."+coin[0]+"&count=60&to=2021-01-"+day+"%20"+hour+":00:00", headers=headers)
            tradedata = r.json()

            for trade in reversed(tradedata):
                time = trade['candleDateTime']
                timedata = time[0:10] + " " + time[11:16]
                op = trade['openingPrice']  # op 는 시작 가격
                tp = trade['tradePrice']  # tp 는 종가
                lp = trade['lowPrice']  # lp 는 저가
                hp = trade['highPrice']  # hp 는 고가
                box[timedata] = [op,hp,lp,tp]

    tradedata = pd.DataFrame(box)
    tradedata.rename(index={0: "Open Price", 1: "High Price", 2: "Low Price", 3: 'Close Price'}, inplace=True)
    transposed_tradedata = tradedata.transpose()
    transposed_tradedata.to_excel(excel_writer='C:/Users/whdtlr/Bitcoin_desktop/Jan_coin/'+coin[1]+'.xlsx')
    print(coin[1])
    cycle+=1
    if cycle%5==0:
        sleep(35)
        print("-------waiting-------")
