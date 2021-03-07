# Image classifier with Keras
from keras.models import Sequential
from keras.layers import Dense

# Shape of our training data is (50, 28, 28, 1)
# which is 50 images (at 28x28) with only one channel/color, black/white
print(train_data.shape)

model = Sequential()
# First layer is connected to all pixels in original image
model.add(Dense(10, activation='relu', 
				  input_shape=(784,)))

# 28x28 = 784, so one input from every pixel
# More info on the Dense layer args: https://keras.io/api/layers/core_layers/dense/
# First arg is units which corresponds to dimensions of output
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))

# Unlike hidden layers, output layer has 3 for output (for 3 classes well classify)
# and a softmax layer which is used for classifiers
model.add(Dense(3, activation='softmax'))

# Model needs to be compiled before it is fit.  loss tells it to optimize for classifier
model.compile(optimizer='adam',
						  loss='categorical_crossentropy',
						  metrics=['accuracy'])

# Prepare data (needs to be tabular so 50 rows and 784 cols)
train_data = train_data.reshape((50, 784))

# Fit model
# To avoid overfiting we set aside 0.2 of images for validation set
# We'll send data through NN 3 times (epochs) and test on that validation set
model.fit(train_data, train_labels,
	 			  validation_split=0.2,
	 			  epochs=3)

# Evaluate on test set that's not evaluation set using the evaluation function
test_data = test_data.reshape((10, 784))
model.evaluate(test_data, test_labels)



