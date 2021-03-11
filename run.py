import requests
from pandas import DataFrame
import pandas as pd                     # 주석 해제는 Crtl + /
                                        # 코인에 따라서 주소!!!! 폴더명!!!! 바꿀 것!!

# 코인 이름 / 단위 정리
# Bitcoin / BTC
# Ethereum / ETH
# Ripple / XRP
# Litecoin / LTC
# BitcoinCash / BCH


day = ['31','30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
month = ['12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
# year = ['2018','2019','2020']
year = ['2018','2019','2020']
# for i in range(1,31):
#     num = format(i,'02')
#     list.append(num)
# print(list)                           # 여기는 날짜 리스트 변환


for k in year:
    for j in month:
        tradedata = {}
        for i in day:                                                                                           # 여기 아래 KRW-@@@ 바꿔줘야됨!!!!!!!!!!
            r = requests.get("https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/10?code=CRIX.UPBIT.KRW-BTC&count=144&to="+k+"-"+j+"-"+i+"%2000:00:00")
            bitcoins = r.json()

            for bitcoin in bitcoins:
                time = bitcoin['candleDateTime']
                timedata = time[0:10]+" "+time[11:16]
                op = bitcoin['openingPrice']        # op 는 시작 가격
                tp = bitcoin['tradePrice']          # tp 는 종가
                lp = bitcoin['lowPrice']            # lp 는 저가
                hp = bitcoin['highPrice']           # hp 는 고가
                tradedata[timedata] = [op,tp,hp,lp]

        tradedata = pd.DataFrame(tradedata)
        tradedata.rename(index={0:"Opening Price",1:"Trade Price", 2:"High Price",3:'Low Price'},inplace=True)
        transposed_tradedata = tradedata.transpose()
        reversed_tradedata = transposed_tradedata.iloc[::-1]
        reversed_tradedata.to_excel(excel_writer='C:/Users/whdtlr/github/Bitcoin_desktop/Bitcoin/'+k+'_'+j+'.xlsx')         # 코인이름에 따라 폴더명 변경할 것!!