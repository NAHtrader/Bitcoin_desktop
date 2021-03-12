import pandas as pd
import math


coins=['Ripple','Bitcoin','BitcoinCash','Ethereum','Litecoin']                          # 코인 추가할거면 하세요!!


for coin in coins:
    df = pd.read_excel("C:/Users/whdtlr/github/Bitcoin_desktop/18-20_10m/18-20_"+coin+".xlsx")

    num_index = len(df.index)

    TR = []
                                    # 그리고 len() 함수는 1 크니까 for 문에서 그대로 써도 됨
    for i in range(0, num_index):     # 가로 열 / 세로 행 - Counting이 중요!! 위에 헤더는 빼고 생각
        if i==0:
            type1 = (df.iloc[i+1, 3] - df.iloc[i+1, 4])
            type2 = abs(df.iloc[i+1, 3] - df.iloc[i, 2])
            type3 = abs(df.iloc[i+1, 4] - df.iloc[i, 2])

            TR.append(max(type3, type2, type1))
        else:
            type1=(df.iloc[i,3]-df.iloc[i,4])
            type2=abs(df.iloc[i,3]-df.iloc[(i-1),2])
            type3=abs(df.iloc[i,4]-df.iloc[(i-1),2])

            TR.append(max(type3, type2, type1))

    df["TR"]=TR
    df.columns.values[0] = 'Date'
    df.to_excel(excel_writer='C:/Users/whdtlr/github/Bitcoin_desktop/18-20_10m/18-20_'+coin+'_verTR.xlsx',index=0)


