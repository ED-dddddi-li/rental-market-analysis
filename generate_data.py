import pandas as pd
import numpy as np
import os

np.random.seed(42)
n = 500

districts = ['浦东新区', '徐汇区', '静安区', '长宁区', '普陀区', '杨浦区', '闵行区', '宝山区', '嘉定区', '松江区']
room_types = ['一室一厅', '两室一厅', '两室两厅', '三室一厅', '三室两厅']
subway = ['近地铁（500m内）', '较近地铁（500-1000m）', '较远地铁（1000m以上）']

base_price = {
    '浦东新区': 7500, '徐汇区': 8500, '静安区': 9500, '长宁区': 8000, '普陀区': 6500,
    '杨浦区': 6000, '闵行区': 5500, '宝山区': 4500, '嘉定区': 4000, '松江区': 3800
}
room_price = {'一室一厅': 0, '两室一厅': 1500, '两室两厅': 2000, '三室一厅': 2500, '三室两厅': 3000}

district_col = np.random.choice(districts, n)
room_col = np.random.choice(room_types, n, p=[0.3, 0.35, 0.15, 0.15, 0.05])
subway_col = np.random.choice(subway, n, p=[0.4, 0.35, 0.25])
area_col = np.random.randint(30, 150, n)

price_col = []
for i in range(n):
    base = base_price[district_col[i]] + room_price[room_col[i]]
    if subway_col[i] == '近地铁（500m内）':
        base *= 1.15
    elif subway_col[i] == '较近地铁（500-1000m）':
        base *= 1.05
    noise = np.random.normal(0, 500)
    price_col.append(max(1500, int(base + noise)))

df = pd.DataFrame({
    '区域': district_col,
    '户型': room_col,
    '地铁距离': subway_col,
    '面积(㎡)': area_col,
    '月租金(元)': price_col
})

os.makedirs('data', exist_ok=True)
df.to_csv('data/shanghai_rental.csv', index=False, encoding='utf-8-sig')
print(f"数据生成完成！共 {n} 条记录")
print(df.head())