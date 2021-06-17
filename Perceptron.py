import numpy as np
class Perceptron(object):
  """パーセプトロンの分類器
  
  パラメータ
  --------------
  eta : float
    学習率（0.0より大きく1.0以下の値）
  n_iter : int
    トレーニングデータのトレーニング回数
  random_state : int
    重みを初期化するための乱数シード
    
  属性
  --------------
  w_ : 1次元配列
    適合後の重み
  errors_ : リスト
