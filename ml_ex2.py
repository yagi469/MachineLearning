from scipy import sparse

# 対角成分が1でそれ以外が0の、2次元NumPy配列を作る
eye = np.eye(4)
print("NumPy array:\n{}".format(eye))

# NumPy配列をScipyのCSR形式の疎行列に変換する
# 非ゼロ要素だけが格納される
sparse_matrix = sparse.csr_matrix(eye)
print("\nScipy sparse CSR matrix:\n{}".format(sparse_matrix))

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation:\n{}".format(eye_coo))
