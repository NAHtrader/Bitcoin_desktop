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


max_box=[]
min_box=[]


local_max=donchian_max(df,i,기간)
local_min=donchian_min(df,i,기간)
max_box.append(local_max)
min_box.append(local_min)

df["donchian Max"]=max_box
df["donchina min"]=min_box


### 현재 기간 수정 안되있음 !!!!!