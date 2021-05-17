import pandas as pd
import requests  # version - 2.22.0
import time

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

coin_names = call_coin()
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ함수 입력 칸ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 추가하고 싶은 지표를 함수화해서 입력할 것


for coin in coin_names:
    start = time.time()  # 시작 시간 저장
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ추가하고 싶은 지표ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 리스트로 해서 Column에 추가하는 방식으로 진행 /  Ex. df["factor"] = factor list
    new_dict={}
    new=[]

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ엑셀 불러오기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    df = pd.read_excel('C:/Users/whdtlr/Bitcoin_desktop/march_15m/bolinger/'+coin[1]+'.xlsx')
    num_index = len(df.index)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ반복문을 통해 추가하기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 카운팅 쉽게 하기 위해 앞뒤 각각 100개 잘라내버리기
# 매매 알고리즘 잘 입력할 것!!
    for i in range(0, num_index):
        if df.iloc[i,3]<df.iloc[i,10] and df.iloc[i,1]>df.iloc[i,10]:
            new.append(df.iloc[i,0])
    print(new)




        # if df.iloc[i,5]>df.iloc[i,6] and df.iloc[i,5]>df.iloc[i-1,5] and df.iloc[i,6]>df.iloc[i-1,6]:
        #     if df.iloc[i-1,7]<df.iloc[i,4]:
        #         target_value = df.iloc[i - 1, 7]
        #         target_percent_list=[]
        #         for k in range(0,31):
        #             target_percent_value=df.iloc[i-60+4*k,4]/target_value
        #             target_percent_list.append(target_percent_value)
        #         new_dict[df.iloc[i,0]]=target_percent_list
        #     else:
        #         pass
        # else:
        #     pass


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ엑셀 저장ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    # backtest=pd.DataFrame(new_dict)
    # backtest.to_excel(excel_writer='C:/Users/whdtlr/Bitcoin_desktop/march_15m/backtest/'+coin[1]+'.xlsx', index=False)
    #
    # testing_time = (time.time() - start)
    # print(testing_time)

