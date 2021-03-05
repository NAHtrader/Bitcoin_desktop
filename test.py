import pandas as pd
import math

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

yr=['2018','2019','2020']
month=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
coins=['Ripple','Bitcoin','BitcoinCash','Ethereum','Litecoin']                          # 코인 추가할거면 하세요!!


for coin in coins:
    trade_result = {}
    for y in yr:
        for m in month:
            df = pd.read_excel("C:/Users/admin/Desktop/AT/tradedata/"+coin+"/"+y+"_"+m+".xlsx")
            num_index = len(df.index)
            start = 500000
            total_profit = []
            lose = 0
            win = 0
            for i in range(11, num_index - 2):
                # date = df.iloc[i, 0]
                # op_a = df.iloc[i, 1]  # op 는 시작 가격
                # tp_a = df.iloc[i, 2]  # tp 는 종가
                # hp_a = df.iloc[i, 3]  # hp 는 고가
                # lp_a = df.iloc[i, 4]  # lp 는 저가

# ------------------------------------------------------------------------------------------
                # 이동 평균 구하기
                ms_10 = 0
                ms_10_past = 0
                for k in range(0, 10):
                    ms_10 += df.iloc[(i - k-1), 2]
                    ms_10_past += df.iloc[(i - k - 2), 2]
                ma_10 = ((ms_10) / 10)
                ma_10_past = ((ms_10_past) / 10)
# ------------------------------------------------------------------------------------------
                # 백테스팅 매매 조건식
                if df.iloc[i, 3]> ma_10 and df.iloc[i, 1]<ma_10 and ma_10>ma_10_past:

                    buy_num = (start / ma_10)
                    sell = (df.iloc[(i + 2), 1] * buy_num)
                    profit = (sell - start)
                    profit_ratio = (sell / start)

                    total_profit.append(profit_ratio)
                    if profit < 0:
                        lose += 1
                    else:
                        win += 1
# ------------------------------------------------------------------------------------------
            # 산술 평균 / 기하 평균 구하기
            total_multiple_ratio = multiplyList(total_profit)
            total_sum_ratio = sum(total_profit)
            Geometric_mean_ratio = (total_multiple_ratio ** (1 / len(total_profit)))
            Arithmetic_mean_ratio = (total_sum_ratio / len(total_profit))
# ------------------------------------------------------------------------------------------
            # 승률 및 등장확률 구하기
            # 딕셔너리 저장
            win_ratio = (win / (win + lose) * 100)
            trade_ratio = (len(total_profit) / num_index)*100
            trade_result[str(y)+"_"+str(m)]= [Arithmetic_mean_ratio,Geometric_mean_ratio,trade_ratio,win_ratio]
# ------------------------------------------------------------------------------------------
    # 엑셀 파일 저장
    trade_result = pd.DataFrame(trade_result)
    trade_result.rename(index={0: "산술평균", 1: "기하평균", 2:'등장확률', 3:"승률"}, inplace=True)
    transposed_trade_result = trade_result.transpose()
    reversed_trade_result = transposed_trade_result.iloc[::-1]
    reversed_trade_result.to_excel(excel_writer='C:/Users/admin/Desktop/AT/tradedata/Result/'+coin+'_Result.xlsx')









