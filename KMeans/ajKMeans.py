"""
This program implements the K Means algorithm 
The algorithm takes MNIST dataset and classifies the data
Author: Ajay Krishna Teja Kavuri
"""

#Import the MNIST dataset using a handy program provided by tensorflow
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#Importing the required librararies
import tensorflow as tf
import matplotlib.pyplot as plt


#Placeholder for the data points
x=tf.placeholder(tf.float32,[None,784])

#Actual function
#Initialize the variables
init=tf.initialize_all_variables()

#Obtain the session
ajSess=tf.InteractiveSession()
ajSess.run(init)
for i in range(1000):
	batch_xs, batch_ys=mnist.train.next_batch(100)
	ajSess.run(x,feed_dict={x:batch_xs})




