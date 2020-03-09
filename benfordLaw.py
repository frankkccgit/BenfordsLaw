from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd 
import re

def benfordLaw(list_data, title): # 輸入參數為 資料list, 標題名稱
    
    total = len(list_data) # 資料中總共有多少組數
    benfordList = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6] #這是 Benford Law 的分布
    
    # 處理首位數字
    first_nums = [ int(str(num)[0]) for num in list_data ]
    # 依次取出每個資料轉為string，利用切片取出的首位字，再轉回int，加到list中
    first_nums.sort() # 讓數列排序
    count = Counter(first_nums) # 計算出每個數字共有幾個
    for key in count:
        count[key] = round((count[key]/total*100),2) # 將計數轉換為佔總數的百分比，取兩位小數點
    
    # 畫出數值比較表格
    table = pd.DataFrame(count, index=[title])
    table.loc['Benford List'] = benfordList
    print(table)
    
    #畫出資料 長條圖 與 Benford's Law 的分布曲線比較
    x = list(count.keys()) # x軸使用count的index
    plt.style.use('ggplot')
    
    plt.plot(x, benfordList, label='Benford\'s Distribution', color='blue') #這是Benford's Law分布曲線
    plt.bar(count.keys(), count.values()) #這是資料的長條圖
    
    plt.title(title)
    plt.ylabel('Percentage')
    plt.xlabel('Number')
    plt.xticks(x)
    plt.legend()
    plt.show()
