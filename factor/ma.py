
box=[]
ma=0
for i in range(0,n):
    box.append(df.iloc[t-i,3])
ma=(sum(box)/len(box))
ma_60_box.append(ma)



def moving_average(df,t,n,ma):
    moving_average=0
    moving_average=((ma[t-401]*n)-df.iloc[t-n,4]+df.iloc[t,4])/n
    return moving_average


ma_60_box=[]
ma_240_box=[] # 그리고 len() 함수는 1 크니까 for 문에서 그대로 써도 됨


ma_60=moving_average(df,i,60,ma_60_box)
ma_240=moving_average(df,i,240,ma_240_box)
ma_60_box.append(ma_60)
ma_240_box.append(ma_240)

df["ma_low_60"] = ma_60_box
df["ma_low_240"] = ma_240_box
