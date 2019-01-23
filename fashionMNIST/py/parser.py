# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 17:52:04 2016

@author: kazu
"""
import numpy as np
import os
import cv2
import gzip
import pickle



def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,'{}-labels-idx1-ubyte.gz'.format(kind))
    images_path = os.path.join(path,'{}-images-idx3-ubyte.gz'.format(kind))

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)
    return images, labels

if __name__ == '__main__':
    train_images, train_labels = load_mnist("",kind='train')
    count = 0
    for image, label in zip(train_images, train_labels):
        if not os.path.exists("data/train/{}".format(label)):
            os.makedirs("data/train/{}".format(label))
        image = np.reshape(image, (28,28)).astype(np.uint8)
        cv2.imwrite("data/train/{0}/{1:05d}.png".format(label,count),image)
        count+=1

    test_images, test_labels = load_mnist("",kind='t10k')
    count = 0
    for image, label in zip(test_images, test_labels):
        if not os.path.exists("data/test/{}".format(label)):
            os.makedirs("data/test/{}".format(label))
        image = np.reshape(image, (28,28)).astype(np.uint8)
        cv2.imwrite("data/test/{0}/{1:05d}.png".format(label,count),image)
        count+=1
