from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras.optimizers import SGD

from tensorflow.keras.datasets import mnist

from tensorflow.keras import backend as K

import matplotlib.pyplot as plt

import numpy as np

model = Sequential()
model.add(InputLayer(input_shape=(15,16)))
model.add(Dense(15,activation=relu))