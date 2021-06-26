import pandas as pd

# 人を表す簡単なデータセットを作る
data = {'Name': ["John", "Anna", "Peter", "Linda"],
        'Location':["New York", "Paris", "Berlin", "London"],
        'Age':[24, 13, 53, 33]
       }

data_pandas = pd.DataFrame(data)

# IPython.displayを用いるとDataFrameを
# Jupyter notebook上できれいに表示することができる。
display(data_pandas)

# ageカラムが30を超えるすべての行を取り出す
display(data_pandas[data_pandas.Age > 30])
