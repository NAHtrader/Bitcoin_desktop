import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/whdtlr/Bitcoin_desktop/Feb_coin/backtest/Just.xlsx")
data = pd.DataFrame(df)

                                         # kind 예시 : line , bar , scatter
df.plot(kind = 'line', legend=False)

# x & y 에 Header 를 입력해야함!!
plt.show()
