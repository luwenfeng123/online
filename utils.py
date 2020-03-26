# -*-coding：utf-8-*-
# @Time         :2020/3/6/9:58
# @Author       :Lwf
# @Email        :S
# @File         :utils.py
# 导入pandas数据包
import pandas as pd


# 定义数据处理函数
def clean_df(df, training=True):
    df = df.drop(['site_id', 'app_id', 'device_id', 'device_ip', 'site_domain',
                  'site_category', 'app_domain', 'app_category', 'device_model'], axis=1)
    if training:
        # id column is not required for training purposes
        df = df.drop(['id'], axis=1)

    return df


# 定义数据加载函数
def load_df(filename, training=True, **csv_options):
    df = pd.read_csv(filename, header=0, **csv_options)
    df = clean_df(df, training=training)
    return df

