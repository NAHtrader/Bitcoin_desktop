import pandas as pd
import math

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result



df = pd.read_excel("C:/Users/admin/Desktop/AT/tradedata/Ripple/2020_12.xlsx")

num_index = len(df.index)

start = 500000

total_profit = []
lose = 0
win = 0
buy_commission = 0
sell_commission = 0

for i in range(11, num_index - 2):
    date = df.iloc[i, 0]
    op_a = df.iloc[i, 1]  # op 는 시작 가격
    tp_a = df.iloc[i, 2]  # tp 는 종가
    hp_a = df.iloc[i, 3]  # hp 는 고가
    lp_a = df.iloc[i, 4]  # lp 는 저가

    ms_10 = 0
    ms_10_past=0
    for k in range(0, 10):
        ms_10 += df.iloc[(i - k-1), 2]
        ms_10_past+= df.iloc[(i-k-2),2]
    ma_10 =( (ms_10) / 10)
    ma_10_past = ((ms_10_past) / 10)

    if hp_a > ma_10 and op_a<ma_10 and ma_10<ma_10_past:

        buy_num =(start / ma_10)
        sell =( df.iloc[(i + 2), 1] * buy_num )
        profit=(sell-start)
        profit_ratio=(sell/start)

        total_profit.append(profit_ratio)
        if profit < 0:
            lose += 1
        else:
            win += 1

total_multiple_ratio = multiplyList(total_profit)
total_sum_ratio=sum(total_profit)

Geometric_mean_ratio= (total_multiple_ratio**(1/len(total_profit)))
Arithmetic_mean_ratio= (total_sum_ratio/len(total_profit))

