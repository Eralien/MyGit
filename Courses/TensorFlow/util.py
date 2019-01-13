from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf


def read_birth_file(filename):
    title = open(filename, 'r').readlines()[0]
    title = [title[:-1].split('\t')]
    data = open(filename, 'r').readlines()[1:]
    data = [word[:-1].split('\t') for word in data]
    nation = [str(word[0]) for word in data]
    birtio = [float(word[1]) for word in data]
    lifexp = [float(word[2]) for word in data]
    data = zip(birtio, lifexp)
    len_data = len(data)
    data = np.asarray(data, dtype=np.float32)
    return title, data, len_data, nation

def huber_loss(ground, pred, delta=15.0):
    residual = tf.abs(ground - pred)
    def f1(): return 0.5 * tf.square(residual)
    def f2(): return delta * tf.abs(residual) - 0.5 * tf.sqare(delta)
    return tf.cond(residual > delta, f2, f1)