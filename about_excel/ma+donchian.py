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

def moving_average(df,t,n,ma):
    moving_average=0
    moving_average=((ma[t-401]*n)-df.iloc[t-n,3]+df.iloc[t,3])/n
    return moving_average

def donchian_max(df,t,N):   # t 는 시점 (건들지 말 것!)
  box=[]    # N은 기간 (N을 조정할 것!)
  max_value=0
  for i in range(0,N):
    box.append(df.iloc[(t-N+i),2]) # 데이터 프레임 카운팅 주의
  max_value=max(box)
  return max_value

def donchian_min(df,t,N):
  box=[]
  min_value=0
  for i in range(0,N):
      box.append(df.iloc[(t-N+i),3]) # 데이터 프레임 카운팅 주의
  min_value=min(box)
  return min_value

for coin in coin_names:
    start = time.time()  # 시작 시간 저장
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ추가하고 싶은 지표ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 리스트로 해서 Column에 추가하는 방식으로 진행 /  Ex. df["factor"] = factor list
    ma_60_box = []
    ma_240_box = []
    max_box = []
    min_box = []

    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ엑셀 불러오기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    df = pd.read_excel('C:/Users/whdtlr/Bitcoin_desktop/Jan_coin_4h/'+coin[1]+'.xlsx')
    num_index = len(df.index)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ반복문을 통해 추가하기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 카운팅 쉽게 하기 위해 앞에 400개 잘라내버리기
    for i in range(400, num_index):
        if i == 400:
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

            local_max = donchian_max(df, i, 60)
            local_min = donchian_min(df, i, 60)
            max_box.append(local_max)
            min_box.append(local_min)

        else:
            ma_60 = moving_average(df, i, 60, ma_60_box)
            ma_240 = moving_average(df, i, 240, ma_240_box)
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
    df["donchian min"] = min_box
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ저장 위치 주의!!ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    df.to_excel(excel_writer='C:/Users/whdtlr/Bitcoin_desktop/Jan_coin_4h/donchian+ma/'+coin[1]+'.xlsx',index=0)
    print("Work Done")
    testing_time = (time.time() - start)
    print(testing_time)

