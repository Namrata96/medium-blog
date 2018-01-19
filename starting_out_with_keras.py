# Importing necessary modules
from keras.models import Sequential
from keras.layers import Dense

# Setting up some hyper-parameters
LEARNING_RATE = 1e-3
BATCH_SIZE = 5
NUMBER_EPOCHS = 5


# Function for creating a Keras model
def create_model():
    model = Sequential()
    model.add(Dense(5, input_shape=(10,), kernel_initializer="uniform",activation="relu"))
    model.add(Dense(2, activation='softmax'))
    
    return model

# Creating a Keras model
model = create_model()

# Importing necessary modules
from keras import losses
from keras.optimizers import SGD

# Defining the optimizer
sgd = SGD(lr=1e-3)
# Compiling the model and defining the loss and metric for evaluation.
model.compile(optimizer = sgd, loss='categorical_crossentropy', metrics=['accuracy'])

# Running the Model
model.fit(X, y, verbose=1, epochs=NUMBER_EPOCHS, batch_size=BATCH_SIZE)
