def ATR(df, n1):
    max_value=0
    type1 = (df.iloc[n1, 3] - df.iloc[n1, 4])
    type2 = abs(df.iloc[n1, 3] - df.iloc[(n1 - 1), 2])
    type3 = abs(df.iloc[n1, 4] - df.iloc[(n1 - 1), 2])
    max_value=max(type3, type2, type1)
    return max_value


TR = []


atr=ATR(df,i)
TR.append(atr)

df["TR"]=TR



