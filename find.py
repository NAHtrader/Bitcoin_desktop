import pandas as pd

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

yr=['2018','2019','2020']
month=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for y in yr:
    trade_result={}
    for m in month:
        df = pd.read_excel("C:/Users/kjs01/AT/Bitcoin/"+y+"_"+m+".xlsx")
        num_index = len(df.index)

        start = 500000

        total_profit = []
        charge = []
        lose = 0
        win = 0
        buy_commission = 0
        sell_commission = 0
        for i in range(9, num_index - 2):
            date = df.iloc[i, 0]
            op_a = df.iloc[i, 1]  # op 는 시작 가격
            tp_a = df.iloc[i, 2]  # tp 는 종가
            hp_a = df.iloc[i, 3]  # hp 는 고가
            lp_a = df.iloc[i, 4]  # lp 는 저가
            ms_10 = 0
            for k in range(0, 10):
                ms_10 += df.iloc[(i - k), 2]
            ma_10 =( (ms_10) / 10)
            if hp_a > ma_10:

                buy_num = start / ma_10
                sell = df.iloc[(i + 2), 1] * buy_num
                profit =( sell - start )

                buy_commission = 250
                sell_commission = (sell * 0.0005)

                charge.append(buy_commission)
                charge.append(sell_commission)
                total_profit.append(profit)
                if profit < 0:
                    lose += 1
                else:
                    win += 1

        total_plus = sum(total_profit)
        total_charge = sum(charge)
        win_ratio = (win / (win + lose) * 100)
        trade_num = len(total_profit)
        trade_result[str(y)+"_"+str(m)]= [total_plus,total_charge,trade_num,win_ratio]

    trade_result = pd.DataFrame(trade_result)
    trade_result.rename(index={0: "순수익", 1: "수수료", 2:'거래 횟수', 3:"승률"}, inplace=True)
    transposed_trade_result = trade_result.transpose()
    reversed_trade_result = transposed_trade_result.iloc[::-1]
    reversed_trade_result.to_excel(excel_writer='C:/Users/kjs01/AT/Result/Bitcoin_Result_' + y + '.xlsx')
