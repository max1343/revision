"""
Simple TensorFlow exercises
You should thoroughly test your code
"""

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()


def zero(): return tf.constant(0.)


###############################################################################
# 1a: Create two random 0-d tensors x and y of any distribution.
# Create a TensorFlow object that returns x + y if x > y, and x - y otherwise.
# Hint: look up tf.cond()
# I do the first problem for you
###############################################################################

x = tf.random_uniform([])  # Empty array as shape creates a scalar.
y = tf.random_uniform([])
out = tf.cond(tf.greater(x, y), lambda: tf.add(x, y), lambda: tf.subtract(x, y))
print("out 1: ", sess.run(out))

###############################################################################
# 1b: Create two 0-d tensors x and y randomly selected from the range [-1, 1).
# Return x + y if x < y, x - y if x > y, 0 otherwise.
# Hint: Look up tf.case().
###############################################################################

# YOUR CODE
x2 = tf.random_uniform([], -1, 1, dtype=tf.float32)
y2 = tf.random_uniform([], -1, 1, dtype=tf.float32)
out2 = tf.case({tf.less(x, y): lambda: tf.add(x, y), tf.greater(x, y): lambda: tf.subtract(x, y)}, zero, True)
print("out 2: ", sess.run(out2))

###############################################################################
# 1c: Create the tensor x of the value [[0, -2, -1], [0, 1, 2]] 
# and y as a tensor of zeros with the same shape as x.
# Return a boolean tensor that yields Trues if x equals y element-wise.
# Hint: Look up tf.equal().
###############################################################################

# YOUR CODE
x3 = tf.constant([[0, -2, -1], [0, 1, 2]])
y3 = tf.zeros([2, 3], dtype=tf.int32)
out3 = tf.equal(x3, y3)
print("out 3: ", sess.run(out3))

###############################################################################
# 1d: Create the tensor x of value 
# [29.05088806,  27.61298943,  31.19073486,  29.35532951,
#  30.97266006,  26.67541885,  38.08450317,  20.74983215,
#  34.94445419,  34.45999146,  29.06485367,  36.01657104,
#  27.88236427,  20.56035233,  30.20379066,  29.51215172,
#  33.71149445,  28.59134293,  36.05556488,  28.66994858].
# Get the indices of elements in x whose values are greater than 30.
# Hint: Use tf.where().
# Then extract elements whose values are greater than 30.
# Hint: Use tf.gather().
###############################################################################

# YOUR CODE
x4 = tf.constant([29.05088806,  27.61298943,  31.19073486,  29.35532951,
                  30.97266006,  26.67541885,  38.08450317,  20.74983215,
                  34.94445419,  34.45999146,  29.06485367,  36.01657104,
                  27.88236427,  20.56035233,  30.20379066,  29.51215172,
                  33.71149445,  28.59134293,  36.05556488,  28.66994858])
outWhere = tf.where(x4 > 30)
out4 = tf.gather(x4, outWhere)
print("out 4 : ", sess.run(out4))

###############################################################################
# 1e: Create a diagnoal 2-d tensor of size 6 x 6 with the diagonal values of 1,
# 2, ..., 6
# Hint: Use tf.range() and tf.diag().
###############################################################################

# YOUR CODE
x5 = tf.diag(tf.range(1, 7))
print("out 5: ", sess.run(x5))

###############################################################################
# 1f: Create a random 2-d tensor of size 10 x 10 from normal distribution 
# mean=10 and stdev=1.
# Calculate its determinant.
# Hint: Look at tf.matrix_determinant().
###############################################################################

# YOUR CODE
x6 = tf.random_normal([10, 10], mean=10, stddev=1)
out6 = tf.matrix_determinant(x6)
print("out 6: ", sess.run(out6))

###############################################################################
# 1g: Create tensor x with value [5, 2, 3, 5, 10, 6, 2, 3, 4, 2, 1, 1, 0, 9].
# Return the unique elements in x
# Hint: use tf.unique(). Keep in mind that tf.unique() returns a tuple.
###############################################################################

# YOUR CODE
x7 = tf.constant([5, 2, 3, 5, 10, 6, 2, 3, 4, 2, 1, 1, 0, 9])
out7, i = tf.unique(x7)
print("out 7: ", sess.run(out7))

###############################################################################
# 1h: Create two tensors x and y of shape 300 from any normal distribution,
# as long as they are from the same distribution.
# Use tf.cond() to return:
# - The mean squared error of (x - y) if the average of all elements in (x - y)
#   is negative, or
# - The sum of absolute value of all elements in the tensor (x - y) otherwise.
# Hint: see the Huber loss function in the lecture slides 3.
###############################################################################

# YOUR CODE
x8 = tf.random_normal([300])
y8 = tf.random_normal([300])
out8 = tf.cond(tf.reduce_mean((x - y)) < 0, lambda: tf.reduce_mean(tf.square((x - y))), lambda: tf.reduce_sum(tf.abs(x - y)))
print("out 8: ", sess.run(out8))
