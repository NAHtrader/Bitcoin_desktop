import requests  # version - 2.22.0
import pandas as pd
import time


df = pd.read_excel('C:/Users/whdtlr/Bitcoin_desktop/Jan_coin/Bitcoin.xlsx')
num_index = len(df.index)

start = time.time()  # 시작 시간 저장
def moving_average(df,t,n,ma):
    moving_average=0
    moving_average=((ma[t-401]*n)-df.iloc[t-n,3]+df.iloc[t,3])/n
    return moving_average


ma_60_box = []
ma_240_box = []
max_box = []
min_box = []

for i in range(400, num_index):
    if i==400:
        box1 = []
        ma_60 = 0
        for j in range(0, 60):
            box1.append(df.iloc[i - j, 3])
        ma_60 = (sum(box1) / 60)
        ma_60_box.append(ma_60)

        box2 = []
        ma_240 = 0
        for k in range(0, 240):
            box2.append(df.iloc[i - k, 3])
        ma_240 = (sum(box2) / 240)
        ma_240_box.append(ma_240)


    else:
        ma_60 = moving_average(df, i, 60, ma_60_box)
        ma_240 = moving_average(df, i, 240, ma_240_box)
        ma_60_box.append(ma_60)
        ma_240_box.append(ma_240)

df = df.drop(df.index[0:400])

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ엑셀 저장ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
df["ma_low_60"] = ma_60_box
df["ma_low_240"] = ma_240_box
# df["donchian Max"] = max_box
# df["donchina min"] = min_box
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ저장 위치 주의!!ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
df.to_excel(excel_writer='C:/Users/whdtlr/Bitcoin_desktop/Jan_coin/donchian+ma/Bitcoin.xlsx',index=0)
print("Work Done")
testing_time = (time.time() - start)
print(testing_time)
