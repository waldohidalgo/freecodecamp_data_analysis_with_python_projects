import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
# df['overweight'] = pd.cut(df['weight']/(df['height']/100)**2,bins=[0,25,np.inf],labels=[0,1])
df['overweight']=np.where(df['weight']/(df['height']/100)**2<=25,0,1)

# 3
#df['gluc']=pd.cut(df['gluc'],bins=[0,1,np.inf],labels=[0,1])
#df['cholesterol']=pd.cut(df['cholesterol'],bins=[0,1,np.inf],labels=[0,1])

df['gluc']=np.where(df['gluc'] <= 1, 0, 1)
df['cholesterol']=np.where(df['cholesterol']<=1,0,1)

# 4
def draw_cat_plot():
    # 5
    variables=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=variables)

    # 6
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index().rename(columns={0:'total'})
    
    # 7

    # 8
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio",  kind="bar", height=4, aspect=1.5 ).figure

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    f1=(df['ap_lo'] <= df['ap_hi'])
    f2=(df['height'] >= df['height'].quantile(0.025))
    f3=(df['height'] <= df['height'].quantile(0.975))
    f4=(df['weight'] >= df['weight'].quantile(0.025))
    f5=(df['weight'] <= df['weight'].quantile(0.975))

    # 11
    df_heat = df[f1 & f2 & f3 & f4 &f5]

    # 12
    corr = df_heat.corr()

    # 13
    mask=np.triu(np.ones(corr.shape), 0).astype(bool)

    # 14
    fig, ax =plt.subplots(figsize=(12, 6))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, linewidths=0.5, ax=ax,cmap='inferno',fmt=".1f")

    # 16
    fig.savefig('heatmap.png')
    return fig


# if __main__=="medical_data_visualizer":
#     fig=draw_heat_map()

#     res=[]
#     for label in fig.axes[0].get_xticklabels():
#     res.append(label.get_text())
#     print(res)