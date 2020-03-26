# -*-coding：utf-8-*-
# @Time         :2020/3/6/9:58
# @Author       :Lwf
# @Email        :S
# @File         :predict.py
# 导包
from pandas import DataFrame
import joblib
import numpy as np

from utils import load_df


#  按照指定的格式生成结果
def create_submission(ids, predictions, filename='submission.csv'):
    submissions = np.concatenate((ids.reshape(len(ids), 1), predictions.reshape(len(predictions), 1)), axis=1)
    df = DataFrame(submissions)
    df.to_csv(filename, header=['id', 'click'], index=False)


classifier = joblib.load('classifier.pkl')
test_data_df = load_df('csv/test.csv', training=False)
print(test_data_df)
ids = test_data_df.values[0:, 0]
print(ids)
predictions = classifier.predict(test_data_df.values[0:, 1:])
print(predictions)
create_submission(ids, predictions)
