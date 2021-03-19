import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/whdtlr/github/Bitcoin_desktop/18-20_10m/18-20_ripple_verTR.xlsx")
data = pd.DataFrame(df)
                                                    # kind 예시 : line , bar , scatter
df.plot(x ='Date', y='TR', kind = 'line')       # x & y 에 Header 를 입력해야함!!
plt.show()
