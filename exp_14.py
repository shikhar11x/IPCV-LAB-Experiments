# Experiment 14: CNN for Image Classification

import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential([
layers.Conv2D(32,(3,3),activation='relu',input_shape=(64,64,3)),
layers.MaxPooling2D((2,2)),
layers.Flatten(),
layers.Dense(64,activation='relu'),
layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])

