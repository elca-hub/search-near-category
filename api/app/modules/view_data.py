import pandas as pd
import pylab
from matplotlib import pyplot
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
import csv

def make_category ():
  csv_path = './modules/csv/data.csv'
  res_path = './modules/csv/res.csv'
  # 以下の形式のcsvファイルからデータフレームを作成
  # id
  # name
  # fun
  # sad
  # imp
  # ang
  df = pd.read_csv(csv_path, header=0, index_col=0, usecols=['id', 'fun', 'sad', 'imp', 'ang'])

  # 主成分分析
  pca = PCA(n_components=2)
  pca.fit(df)

  # k-means++でクラスタリング
  kmeans = KMeans(n_clusters=5, init="k-means++")
  kmeans.fit(pca.transform(df))

  # クラスタリング結果を配列に格納
  labels = kmeans.labels_

  # csvファイルを取得
  csv_file = open(csv_path, 'r')

  # idを取得
  name = []
  for row in csv.reader(csv_file):
    # ヘッダー行は無視
    if row[0] == 'id':
      continue
    name.append(row[0])

  # クラスタリング結果とidを結合
  result = np.c_[labels, name]

  # クラスタリング結果をcsvファイルに出力
  with open(res_path, 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['cluster', 'id'])
    writer.writerows(result)
