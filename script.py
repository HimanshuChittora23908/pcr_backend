import pandas as pd
from flask import Flask
from flask import jsonify
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)


@app.route('/')
def hello():
    dataset = pd.read_csv('hello.csv')
    X = dataset.iloc[:, [1, 1]].values
    kmeans = KMeans(n_clusters=20, init='k-means++', random_state=42)
    y_kmeans = kmeans.fit_predict(X)
    temp = np.array(y_kmeans)
    index = [0] * 20
    for i, x in enumerate(temp):
        if x == 0:
            index[0] = i
            break
    for i, x in enumerate(temp):
        if x == 1:
            index[1] = i
            break
    for i, x in enumerate(temp):
        if x == 2:
            index[2] = i
            break
    for i, x in enumerate(temp):
        if x == 3:
            index[3] = i
            break
    for i, x in enumerate(temp):
        if x == 4:
            index[4] = i
            break
    for i, x in enumerate(temp):
        if x == 5:
            index[5] = i
            break
    for i, x in enumerate(temp):
        if x == 6:
            index[6] = i
            break
    for i, x in enumerate(temp):
        if x == 7:
            index[7] = i
            break
    for i, x in enumerate(temp):
        if x == 8:
            index[8] = i
            break
    for i, x in enumerate(temp):
        if x == 9:
            index[9] = i
            break
    for i, x in enumerate(temp):
        if x == 10:
            index[10] = i
            break
    for i, x in enumerate(temp):
        if x == 11:
            index[11] = i
            break
    for i, x in enumerate(temp):
        if x == 12:
            index[12] = i
            break
    for i, x in enumerate(temp):
        if x == 13:
            index[13] = i
            break
    for i, x in enumerate(temp):
        if x == 14:
            index[14] = i
            break
    for i, x in enumerate(temp):
        if x == 15:
            index[15] = i
            break
    for i, x in enumerate(temp):
        if x == 16:
            index[16] = i
            break
    for i, x in enumerate(temp):
        if x == 17:
            index[17] = i
            break
    for i, x in enumerate(temp):
        if x == 18:
            index[18] = i
            break
    for i, x in enumerate(temp):
        if x == 19:
            index[19] = i
            break

    response = jsonify({'index': index})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
