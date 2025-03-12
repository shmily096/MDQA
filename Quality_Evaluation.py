import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'sample_interview.csv'
sample_data = pd.read_csv(file_path)
# print(sample_data.head())

cols_to_vis = ['criteriaA', 'criteriaB', 'criteriaC', 'TotalPartsInspected']
classifications_to_vis = ['A', 'B', 'C', 'D', 'E']

for col in cols_to_vis:
    # 创建一个新的图形窗口，设置图形大小为宽 10 英寸，高 3 英寸
    plt.figure(figsize=(10, 3)) 
    for classification in classifications_to_vis:
        # Plot the density for the current classification group
        # 从 sample_data 中筛选出当前分类的数据，并选择当前列的数据绘制密度图
        sample_data[sample_data['classification'] == classification][col].plot(kind='density', label=classification)
    
    # 设置 x 轴的范围为 0 到 60
    plt.xlim(0, 60)
    # 显示图例，用于区分不同分类的密度图
    plt.legend()
    # 设置图形的标题，显示当前列的名称和不同分类的分布情况
    plt.title(f'Distribution of {col} for Different Classifications')
    # 显示图形
    plt.show()