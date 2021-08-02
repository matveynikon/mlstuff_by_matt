#First, include following libraries:
# Importing all necessary libraries
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
#Here, the train_data_dir is the train dataset directory. validation_data_dir is the
#directory for validation data. nb_train_samples is the total number train #samples. nb_validation_samples is the total number of validation samples.
img_width, img_height = 224, 224
train_data_dir = 'catdog/dataset/training_set'
validation_data_dir = 'catdog/dataset/test_set'
nb_train_samples =400
nb_validation_samples = 100
epochs = 10
batch_size = 16
#checking the format of the image
if K.image_data_format() == 'channels_first':
   input_shape = (3, img_width, img_height)
else:
   input_shape = (img_width, img_height, 3)
model = Sequential()
#Conv2D is the layer to convolve the image into multiple images
model.add(Conv2D(32, (2, 2), input_shape=input_shape))
#Activation is the activation function.
model.add(Activation('relu'))
#MaxPooling2D is used to max pool the value from the given size #matrix and same is used for the next 2 layers.
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (2, 2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (2, 2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#MaxPooling2D is used to max pool the value from the given size
#matrix and same is used for the next 2 layers.
model.add(Flatten())
#Dense is used to make this a fully connected model and is the
#hidden layer.
model.add(Dense(64))
model.add(Activation('relu'))
#Dropout is used to avoid overfitting on the dataset.
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
#Compile function is used here that involve use of loss, optimizers
#and metrics.here loss function used is binary_crossentropy,
#optimizer used is rmsprop.
model.compile(loss='binary_crossentropy',optimizer='rmsprop', metrics=['accuracy'])
#ImageDataGenerator that rescales the image, applies shear in some
#range, zooms the image #and does horizontal flipping with the
#image. This ImageDataGenerator includes all possible
#orientation
#of the image.
train_datagen = ImageDataGenerator(rescale=1. / 255,shear_range=0.2, zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1. / 255)
#train_datagen.flow_from_directory is the function that is used to
#prepare data from the train_dataset directory Target_size specifies
#the target size of the image.
train_generator = train_datagen.flow_from_directory( train_data_dir,
target_size=(img_width, img_height),batch_size=batch_size,class_mode='binary')
validation_generator = test_datagen.flow_from_directory( validation_data_dir, target_size=(img_width, img_height),
batch_size=batch_size, class_mode='binary')
#fit_generator is used to fit the data into the model made above,
#other factors used are steps_per_epochs tells us about the number
#of times the model will execute for the training data.
#epochs tells us the number of times model will be trained in forward
#and backward pass.
#validation_data is used to feed the validation/test data into the #model.
#validation_steps denotes the number of validation/test samples.
model.fit_generator(train_generator,steps_per_epoch=nb_train_samples // batch_size,
epochs=epochs, validation_data=validation_generator,
validation_steps=nb_validation_samples // batch_size)
#Save the model
model.save_weights('ImgmodelKeras_saved.h5')