import os
import pandas as pd
import time

# 设置环境变量
os.environ['MI_USER'] = 'peterljf@126.com'
os.environ['MI_PASS'] = 'Think9pad'
os.environ['MI_DID'] = '400093670'

# 读取Excel文件
df = pd.read_excel('plan.xlsx')

# 遍历每行数据，并按时间顺序执行COMMAND
for index, row in df.sort_values(by=['DATE', 'TIME']).iterrows():
    # 计算当前时间与执行时间的时间差
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    time_diff = (pd.to_datetime(row['DATE'] + ' ' + row['TIME']) - pd.to_datetime(current_time)).total_seconds()

    # 如果时间差为负数，则说明执行时间已经过去，直接跳过
    if time_diff < 0:
        continue

    # 等待时间差
    time.sleep(time_diff)

    # 执行COMMAND命令
    os.system(row['COMMAND'])
