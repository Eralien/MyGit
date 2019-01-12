"""
This is a simple imitation of its counterpart
"""
import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf 
import os

def read_birth_file(filename):
    title = open(filename, 'r').readlines()[0]
    title = [title[:-1].split('\t')]
    data = open(filename, 'r').readlines()[1:]
    data = [word[:-1].split('\t') for word in data]
    nation = [str(word[0]) for word in data]
    birtio = [float(word[1]) for word in data]
    lifexp = [float(word[2]) for word in data]
    data = zip(nation, birtio, lifexp)
    len_data = len(data)
    data = np.asarray(data, dtype=np.float32)
    return title, data, len_data

"""
The model is like this:
inference: Find a relationship between X and Y to predict Y from X
Inference: Y_predicted = w*X + b
MSE = E[(y - y_predicted)^2]
"""
cwd = os.getcwd()
FILE_PATH = cwd + '/examples/data/birth_life_2010.txt'
_, data, len_data = read_birth_file(FILE_PATH)


pass




