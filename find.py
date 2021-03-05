import pandas as pd
df = pd.read_excel("C:/Users/admin/Desktop/AT/tradedata/Bitcoin/2017_10.xlsx")
# df = df.set_index('Unnamed: 0')

hammer = []
num_index = len(df.index)

for i in range(1,num_index):
    date = df.iloc[i, 0]
    op_today = df.iloc[i, 1]  # op 는 시작 가격
    tp_today = df.iloc[i, 2]  # tp 는 종가
    hp_today = df.iloc[i, 3]  # hp 는 고가
    lp_today = df.iloc[i, 4]  # lp 는 저가


    op_yest = df.iloc[i-1, 1]  # op 는 시작 가격
    tp_yest = df.iloc[i-1, 2]  # tp 는 종가
    hp_yest = df.iloc[i-1, 3]  # hp 는 고가
    lp_yest = df.iloc[i-1, 4]  # lp 는 저가







