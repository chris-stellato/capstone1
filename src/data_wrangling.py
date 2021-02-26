from pyspark.sql.functions import *
import pyspark as ps
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sn
from scipy import stats
import numpy as np
import os
import json
import glob

spark = ps.sql.SparkSession.builder \
            .master("local[4]") \
            .appName("df capstone") \
            .getOrCreate()

path_to_json = "./data/"
json_pattern = os.path.join(path_to_json,'*.json')
file_list = glob.glob(json_pattern)

first_frame = spark.read.json(file_list[0], multiLine=True)
playlist = first_frame.head()[1]
single_playlist = playlist[0]
column_names = single_playlist.__fields__

list_of_frames = []
##modify for desired # of json files to read in
for file in file_list[:20]: 
    current_df = spark.read.json(file, multiLine=True)
    current_playlist = current_df.head()[1]
    current_pframe = pd.DataFrame(current_playlist, columns=column_names)
    list_of_frames.append(current_pframe)

df = pd.concat(list_of_frames)

def make_new_feature(df, numerator, denominator, new_feat_name):
    df[new_feat_name] = df[numerator] / df[denominator]

    return df.head()

def save_to_csv(file_path)    
    df.to_csv(file_path)
    pass

