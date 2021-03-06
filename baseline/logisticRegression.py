# -*- encoding: utf-8 -*

from sklearn.linear_model import LogisticRegression
import numpy as np

import util

'''
Method:
1、预处理数据：对数据进行进行归一化处理，使数据均值为0，方差为1。
3、分割训练集，要有验证集。
'''

def logisticReg(trainData, trainLabel, testData, testLabel, **kwargs):
    clf = LogisticRegression()
    trainData = util.normalization(trainData)
    testData = util.normalization(testData)
    acc_list = []
    acc_max = 0
    ret = []

    # Shuffle 10 times, seems useless for logistic regression
    for i in range(1):
        trainData_shuffle, trainLabel_shuffle = util.shuffle(trainData, trainLabel)
        clf.fit(trainData_shuffle, trainLabel_shuffle)
        acc_i = clf.score(testData, testLabel)
        print("%d acc: " % i, acc_i)
        acc_list.append(acc_i)
        if acc_i > acc_max:
            acc_max = acc_i 
            ret = clf.predict(testData)

    acc = np.mean(np.array(acc_list))
    print("Logistic Regression accuracy: ", acc)
    return ret, acc_max