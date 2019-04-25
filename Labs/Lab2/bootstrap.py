import matplotlib

matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
    x = np.random.choice(sample, (iterations, sample_size))
    data_mean = np.mean(x)
    # print(data_mean)
    iterations_mean = []
    for i in range(iterations):
        y = x[i, :]
        iterations_mean.append(np.mean(y))

    # print(iterations_mean)
    lower, upper = np.percentile(iterations_mean, (2.5, 97.5))
    # print(lower, upper)

    return data_mean, lower, upper


if __name__ == "__main__":
    df = pd.read_csv('./salaries.csv')

    data = df.values.T[1]
    print(data.shape[0])
    boots = []
    for i in range(100, 100000, 1000):
        boot = boostrap(data, data.shape[0], i)
        boots.append([i, boot[0], "mean"])
        boots.append([i, boot[1], "lower"])
        boots.append([i, boot[2], "upper"])

    df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	#print(df_boot)
    sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, 100000)

    sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
    sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')


# print ("Mean: %f")%(np.mean(data))
# print ("Var: %f")%(np.var(data))



### 2nd part
    df_v = pd.read_csv('vehicles.csv')
    df_v_current = df_v.values.T[0]
    #print(boostrap(df_v_current, df_v_current.shape[0], 100))
    boots_v_current = []
    for i in range(100, 100000, 1000):
        boot = boostrap(df_v_current, df_v_current.shape[0], i)
        boots_v_current.append([i, boot[0], "mean"])
        boots_v_current.append([i, boot[1], "lower"])
        boots_v_current.append([i, boot[2], "upper"])

    df_boot_currnet = pd.DataFrame(boots_v_current, columns=['Boostrap Iterations', 'Mean', "Value"])
    # print(df_boot)
    sns_plotx = sns.lmplot(df_boot_currnet.columns[0], df_boot_currnet.columns[1], data=df_boot_currnet, fit_reg=False, hue="Value")

    sns_plotx.axes[0, 0].set_ylim(0, )
    sns_plotx.axes[0, 0].set_xlim(0, 100000)

    sns_plotx.savefig("bootstrap_confidence_current_vehicles.png", bbox_inches='tight')
    sns_plotx.savefig("bootstrap_confidence_current_vehicles.pdf", bbox_inches='tight')


    df_v_new = (df_v.dropna()).values.T[1]
    print(df_v_new.shape)
    #print(boostrap(df_v_new, df_v_new.shape[0], 100))
    boots_new_vehicle = []
    for i in range(100, 100000, 1000):
        boot = boostrap(df_v_new, df_v_new.shape[0],i)
        boots_new_vehicle.append([i, boot[0], "mean"])
        boots_new_vehicle.append([i, boot[1], "lower"])
        boots_new_vehicle.append([i, boot[2], "upper"])

    df_boot_new_vehicle = pd.DataFrame(boots_new_vehicle, columns=['Boostrap Iterations', 'Mean', "Value"])
    # print(df_boot)
    sns_ploty = sns.lmplot(df_boot_new_vehicle.columns[0], df_boot_new_vehicle.columns[1], data=df_boot_new_vehicle, fit_reg=False, hue="Value")

    sns_ploty.axes[0, 0].set_ylim(0, )
    sns_ploty.axes[0, 0].set_xlim(0, 100000)

    sns_ploty.savefig("bootstrap_confidence_new_vehicle.png", bbox_inches='tight')
    sns_ploty.savefig("bootstrap_confidence_new_vehicle.pdf", bbox_inches='tight')


### After comparing the results I have concluded that new fleet is better than current fleet




