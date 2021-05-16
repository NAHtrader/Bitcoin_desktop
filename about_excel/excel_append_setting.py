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
    factor1 = []
    factor2 = []


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ엑셀 불러오기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    df = pd.read_excel('C:/Users/whdtlr/Bitcoin_desktop/Feb_coin/'+coin[1]+'.xlsx')
    num_index = len(df.index)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ반복문을 통해 추가하기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 카운팅 쉽게 하기 위해 앞에 400개 잘라내버리기
    for i in range(400, num_index):
        if i==400:
            # 직접 1회 계산
        else:
            # 점화식 활용!

    df = df.drop(df.index[0:400])

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ엑셀 저장ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    df["Factor 1"] = factor1
    df["Factor2"] = factor2
    df.to_excel(excel_writer='C:/Users/whdtlr/Bitcoin_desktop/Feb_coin/donchian+ma/'+coin[1]+'_donchina.xlsx',index=0)
    print("Work Done")
    testing_time = (time.time() - start)
    print(testing_time)

