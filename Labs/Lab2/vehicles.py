import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('vehicles.csv')
print('pycharm')
print(df.columns)
sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
sns_plot.axes[0,0].set_ylim(0,)
sns_plot.axes[0,0].set_xlim(0,)
sns_plot.savefig("scaterplot_vehicle.png",bbox_inches='tight')
plt.show()


sns_plot2 = sns.distplot(df['Current fleet'], bins=20, kde=False, rug=True).get_figure()
plt.show()
sns_plot2.savefig("current_fleet.png",bbox_inches='tight')


sns_plot3 = sns.distplot(df['New Fleet'].dropna(), bins=20, kde=False, rug=True).get_figure()
plt.show()
sns_plot3.savefig("new_fleet.png",bbox_inches='tight')