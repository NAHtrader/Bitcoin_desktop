import time
import pandas as pd

try_num=1
all_time_data=[]
while try_num<11:

    start = time.time()  # 시작 시간 저장

    for i in range(14, num_index):
        # 함수
    testing_time=(time.time() - start)
    all_time_data.append(testing_time)
    try_num+=1

average_testing_time=(sum(all_time_data)/len(all_time_data))
print(average_testing_time)
