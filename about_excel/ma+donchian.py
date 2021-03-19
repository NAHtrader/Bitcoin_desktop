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

def moving_average(df,t,n2):
    movingsum=0
    moving_average=0
    for y in range(0,n2):
        movingsum+=df.iloc[(t-y-1),3]
    moving_average=movingsum/n2
    return moving_average

def donchian_max(df,t,N):   # t 는 시점 (건들지 말 것!)
  max=df.iloc[(t-N),2]      # N은 기간 (N을 조정할 것!)
  for i in range(1,N):
      if df.iloc[(t-N+i),2] >= max:
          max = df.iloc[(t - N + i), 2]
  return max

def donchian_min(df,t,N):
  min=df.iloc[(t-N),3]
  for i in range(1,N):
      if df.iloc[(t-N+i),3] <= min:
        min = df.iloc[(t-N+i),3]
  return min

for coin in coin_names:
    start = time.time()  # 시작 시간 저장
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ추가하고 싶은 지표ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 리스트로 해서 Column에 추가하는 방식으로 진행 /  Ex. df["factor"] = factor list
    ma_60_box = []
    ma_240_box = []
    max_box = []
    min_box = []

    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ엑셀 불러오기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    df = pd.read_excel('C:/Users/whdtlr/Bitcoin_desktop/Jan_coin/'+coin[1]+'.xlsx')
    num_index = len(df.index)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ반복문을 통해 추가하기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 카운팅 쉽게 하기 위해 앞에 400개 잘라내버리기
    for i in range(400, num_index):
        ma_60 = moving_average(df, i, 60)
        ma_240 = moving_average(df, i, 240)
        ma_60_box.append(ma_60)
        ma_240_box.append(ma_240)
        local_max = donchian_max(df, i, 60)
        local_min = donchian_min(df, i, 60)
        max_box.append(local_max)
        min_box.append(local_min)

    df = df.drop(df.index[0:400])

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ엑셀 저장ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    df["ma_low_60"] = ma_60_box
    df["ma_low_240"] = ma_240_box
    df["donchian Max"] = max_box
    df["donchina min"] = min_box
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ저장 위치 주의!!ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    df.to_excel(excel_writer='C:/Users/whdtlr/Bitcoin_desktop/Jan_coin/donchian+ma/'+coin[1]+'.xlsx',index=0)
    print("Work Done")
    testing_time = (time.time() - start)
    print(testing_time)

