import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

matplotlib.use('Agg')


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed()  # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
    df = pd.read_csv('vehicles.csv')
    print(df)
    sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("scatterplotveh.png", bbox_inches='tight')
    sns_plot.savefig("scatterplotveh.pdf", bbox_inches='tight')

    data = df.values.T[1]
    data1 = df.values.T[0]
    print(data)
    print(data1)
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Var:", np.var(data))
    print("std:", np.std(data))
    print("MAD:", mad(data))

    print("Mean:", np.mean(data1))
    print("Median:", np.median(data1))
    print("Var:", np.var(data1))
    print("std:", np.std(data1))
    print("MAD:", mad(data1))

    plt.clf()
    sns_plot2 = sns.distplot(data, bins=50, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('New Fleet')
    axes.set_ylabel('Count')

    sns_plot2.savefig("histogramvehnew.png", bbox_inches='tight')
    sns_plot2.savefig("histogramvehnew.pdf", bbox_inches='tight')
    plt.clf()
    sns_plot2 = sns.distplot(data1, bins=50, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('Current Fleet')
    axes.set_ylabel('Count')

    sns_plot2.savefig("histogramvehcurrent.png", bbox_inches='tight')
    sns_plot2.savefig("histogramvehcurrent.pdf", bbox_inches='tight')


