import numpy as np
import scipy.sparse

arr = np.zeros((2, 2))
csc = scipy.sparse.csc_matrix([[10, 20], [20, 40]])
# okay?
arr + csc
# error?
arr += csc
