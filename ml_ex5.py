%matplotlib inline
import matplotlib.pyplot as plt

# -10から10までを100ステップに区切った列を配列として生成
x = np.linspace(-10, 10, 100)
# サイン関数を用いて2つ目の配列を生成
x = np.sin(x)
# plot関数は、一方の配列に対して他方の配列をプロットする
plt.plot(x, y, marker="x")
