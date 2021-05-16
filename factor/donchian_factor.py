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


max_box=[]
min_box=[]


local_max=donchian_max(df,i,기간)
local_min=donchian_min(df,i,기간)
max_box.append(local_max)
min_box.append(local_min)

df["donchian Max"]=max_box
df["donchian min"]=min_box


### 현재 기간 수정 안되있음 !!!!!