import pandas as pd
import math



years = ['2018','2019','2020']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
coins=['Ripple','Bitcoin','BitcoinCash','Ethereum','Litecoin']

for coin in coins:
    tradedata = {}
    for year in years:
        for month in months:
            df = pd.read_excel("C:/Users/whdtlr/github/Bitcoin_desktop/"+coin+"/"+year+"_"+month+".xlsx")

            num_index = len(df.index)

            for i in range(0, num_index):
                timedata = df.iloc[i, 0]
                op = df.iloc[i, 1]  # op 는 시작 가격
                tp = df.iloc[i, 2]  # tp 는 종가
                hp = df.iloc[i, 3]  # hp 는 고가
                lp = df.iloc[i, 4]  # lp 는 저가
                tradedata[timedata] = [op, tp, hp, lp]

    tradedata = pd.DataFrame(tradedata)
    tradedata.rename(index={0:"Opening Price",1:"Trade Price", 2:"High Price",3:'Low Price'},inplace=True)
    transposed_tradedata = tradedata.transpose()
    reversed_tradedata = transposed_tradedata.iloc[::-1] # 행 - 열 바꾸기
    reversed_tradedata_2 =reversed_tradedata.loc[::-1]   # 열
    reversed_tradedata_2.to_excel(excel_writer="C:/Users/whdtlr/github/Bitcoin_desktop/18-20_10m/18-20_"+coin+".xlsx")

