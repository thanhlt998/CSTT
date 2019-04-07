import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib

data = pd.read_csv('csv/500_Person_Gender_Height_Weight_Index.csv')
data_visual = pd.read_csv('csv/500_Person_Gender_Height_Weight_Index.csv')

data = data.loc[data['Gender'] == 'Male']
data_visual = data_visual.loc[data_visual['Gender'] == 'Male']


def convert_status_column(x):
    if x['Index'] == 0:
        return 'Extremely Weak'
    elif x['Index'] == 1:
        return 'Weak'
    elif x['Index'] == 2:
        return 'Normal'
    elif x['Index'] == 3:
        return 'Overweight'
    elif x['Index'] == 4:
        return 'Obesity'
    elif x['Index'] == 5:
        return 'Extremely Obesity'


data_visual['Status'] = data_visual.apply(convert_status_column, axis=1)


def convert_gender_to_label(x):
    if x['Gender'] == 'Male':
        return 1
    if x['Gender'] == 'Female':
        return 0


data_visual['gender_b'] = data_visual.apply(convert_gender_to_label, axis=1)

sns.set_style('whitegrid')

sns.lmplot(x='Height', y='Weight', data=data_visual,
           fit_reg=False,
           hue='Status',
           legend=False,
           palette='Set1',
           size=8,
           aspect=1
           )
ax1 = plt.gca()
ax1.set_title('Height vs Weight', size=15)

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height * 0.9])

ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 15})
plt.show()
# corr = data_visual.corr()
# mask = np.zeros_like(corr)
# mask[np.triu_indices_from(mask)] = True
# fig, ax = plt.subplots(figsize=(10, 10))
# with sns.axes_style("white"):
#     sns.heatmap(corr, mask=mask, cmap="Dark2", annot=True)
#     plt.title("Correlation")
#     plt.show()
# fig, ax = plt.subplots(figsize=(10, 10))
# with sns.axes_style("white"):
#     sns.boxplot(data=data_visual, x='Status', y='Weight', hue='Gender', color="Green")
#     sns.swarmplot(data=data_visual, x='Status', y='Weight', hue='Gender', color="Yellow")
#     plt.title("Gender wise Status Distribution based on weight")
#     plt.plot()
#     plt.show()
# fig, ax = plt.subplots(figsize=(10, 10))
# with sns.axes_style("white"):
#     sns.boxplot(data=data_visual, x='Status', y='Height', hue='Gender', color="Pink", notch=True, width=.5)
#     sns.swarmplot(data=data_visual, x='Status', y='Height', hue='Gender', color="Blue", alpha=.7)
#     plt.title("Gender wise Status Distribution based on weight")
#     plt.plot()
#     plt.show()
