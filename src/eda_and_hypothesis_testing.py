import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from scipy import stats
import numpy as np
import statsmodels.api as sm
import pylab
import statsmodels.stats.weightstats as ws


#read in csv and return pandas dataframe
def csv_to_pdframe(file_path):   
    return pd.read_csv(file_path)


#test chosen pandas series for normal distribution
#saves two figures (box plot and histogram) to PWD and returns Shapiro Wilk test result
def test_for_normal(pandas_dframe, feature_name):

    #box plot
    fig, ax = plt.subplots(figsize=(5,3))
    pandas_dframe.feature_name.plot(kind='box')
    ax.set_title('diversity ratio', fontsize=14)
    fig.savefig('box_plot.png', dpi=300)

    #histogram
    fig, ax = plt.subplots(figsize=(5,3))
    pandas_dframe.feature_name.hist()
    ax.set_xlabel('diversity ratio', fontsize=14)
    fig.savefig('histogram.png', dpi=300)

    #Shapiro Wilk test
    return stats.shapiro(pandas_dframe.feature_name.sample(500))


#save a heatmap figure and return a correlation dataframe
def correlation_eda(pandas_dframe):
    
    #saving heatmap
    fig, ax = plt.subplots(figsize=(10,6))
    sn.set(font_scale=1)
    sn.heatmap(pandas_dframe.corr(), annot=True)
    fig.savefig('heatmap.png', dpi=300)

    #returning correlation matrix
    return pandas_dframe.corr()


#dividing chosen feature into two dataframes, storing them in two variables and printing out some key stats
#feature_value is the value point at which the feature data will be divided. 
def divide_data(df, groupby_feature, measure_feature, grouping_value):
    less_than = df[df['groupby_feature'] < grouping_value]
    greater_equal = df[df['groupby_feature'] >= grouping_value]

    print (f'{groupby_feature} less than {grouping_value}, {measure_feature}: \n mean {less_than.measure_feature.mean()} \n std {less_than.measure_feature.std()} \n \n')

    print (f'{groupby_feature} greater or equal to {grouping_value}, {measure_feature}: \n mean {greater_equal.measure_feature.mean()} \n std {greater_equal.measure_feature.std()} \n \n')

    pass


#bootstrapping helper functions
def bootstrap(data, num_samps=1000):
    return [data.sample(len(data), replace=True) for i in range(num_samps)]

def bootstrap_ci(boot_samp_list, ci=95):
    boot_strap_means = []
    
    for samp in boot_samp_list:
        boot_strap_means.append(np.mean(samp))
        
    left_endpoint = np.percentile(boot_strap_means, (100-ci)/2)
    right_endpoint = np.percentile(boot_strap_means, 100-((100-ci)/2))
    
    return left_endpoint, right_endpoint

def bootstrap_list_of_means(df, measure_feature):
    df_sample_list = np.array(bootstrap(df.measure_feature, 1000))
    return df_sample_list.mean(axis=1)


#returns the left and right endpoints for confidence interval for a bootstrapped sample set
def confidence_interval(df, measure_feature)

    print ('left, right \n')
    return bootstrap_ci(bootstrap(df.measure_feature))


