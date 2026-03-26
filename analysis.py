import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os

# 解决中文显示问题
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('data/shanghai_rental.csv')
os.makedirs('output', exist_ok=True)

print("=== 数据基本信息 ===")
print(f"共 {len(df)} 条租房记录")
print(f"平均月租金：{df['月租金(元)'].mean():.0f} 元")
print(f"最高月租金：{df['月租金(元)'].max()} 元")
print(f"最低月租金：{df['月租金(元)'].min()} 元")

# 图1：各区域平均租金对比
fig, ax = plt.subplots(figsize=(12, 6))
district_avg = df.groupby('区域')['月租金(元)'].mean().sort_values(ascending=False)
colors = sns.color_palette("RdYlGn_r", len(district_avg))
bars = ax.bar(district_avg.index, district_avg.values, color=colors, edgecolor='white', linewidth=0.5)
for bar, val in zip(bars, district_avg.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 80,
            f'{val:.0f}元', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.set_title('上海各区域平均月租金对比', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('区域', fontsize=12)
ax.set_ylabel('平均月租金（元）', fontsize=12)
ax.set_ylim(0, district_avg.max() * 1.15)
ax.grid(axis='y', alpha=0.3)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('output/01_district_avg_price.png', dpi=150, bbox_inches='tight')
plt.close()
print("图1 已生成")

# 图2：户型租金箱线图
fig, ax = plt.subplots(figsize=(11, 6))
order = ['一室一厅', '两室一厅', '两室两厅', '三室一厅', '三室两厅']
palette = sns.color_palette("Blues", len(order))
sns.boxplot(data=df, x='户型', y='月租金(元)', order=order, palette=palette, ax=ax)
ax.set_title('不同户型月租金分布', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('户型', fontsize=12)
ax.set_ylabel('月租金（元）', fontsize=12)
ax.grid(axis='y', alpha=0.3)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('output/02_room_type_price.png', dpi=150, bbox_inches='tight')
plt.close()
print("图2 已生成")

# 图3：地铁距离对租金的影响
fig, ax = plt.subplots(figsize=(9, 6))
subway_avg = df.groupby('地铁距离')['月租金(元)'].mean()
order2 = ['近地铁（500m内）', '较近地铁（500-1000m）', '较远地铁（1000m以上）']
vals = [subway_avg[k] for k in order2]
colors2 = ['#2ecc71', '#f39c12', '#e74c3c']
bars2 = ax.bar(order2, vals, color=colors2, width=0.5, edgecolor='white')
for bar, val in zip(bars2, vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
            f'{val:.0f}元', ha='center', va='bottom', fontsize=11, fontweight='bold')
ax.set_title('地铁距离对月租金的影响', fontsize=16, fontweight='bold', pad=15)
ax.set_ylabel('平均月租金（元）', fontsize=12)
ax.set_ylim(0, max(vals) * 1.15)
ax.grid(axis='y', alpha=0.3)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('output/03_subway_impact.png', dpi=150, bbox_inches='tight')
plt.close()
print("图3 已生成")

# 图4：面积与租金散点图
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(df['面积(㎡)'], df['月租金(元)'], alpha=0.4, c=df['月租金(元)'],
                     cmap='YlOrRd', s=20)
plt.colorbar(scatter, ax=ax, label='月租金（元）')
ax.set_title('租房面积与月租金关系', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('面积（㎡）', fontsize=12)
ax.set_ylabel('月租金（元）', fontsize=12)
ax.grid(alpha=0.3)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('output/04_area_price_scatter.png', dpi=150, bbox_inches='tight')
plt.close()
print("图4 已生成")

print("\n✅ 全部完成！图表保存在 output/ 文件夹中")