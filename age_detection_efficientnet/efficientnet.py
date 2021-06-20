import pandas as pd
import tensorflow as tf
import plotly.graph_objects as go

def load_train(path):
    labels = pd.read_csv(path + '/labels.csv')
    directory = path + '/final_files'
    idg = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=.1/.255,
        validation_split=0.25)
    flow = idg.flow_from_dataframe(
        rescale=1./255.,
        batch_size=8,
        dataframe=labels,
        directory=directory,
        x_col='file_name',
        y_col='real_age',
        subset='training',
        class_mode='raw'
    )
    return flow


def load_test(path):
    labels = pd.read_csv(path + '/labels.csv')
    directory = path + '/final_files'
    idg = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=.1/.255,
        validation_split=0.25)
    flow = idg.flow_from_dataframe(
        rescale=1./255.,
        batch_size=8,
        dataframe=labels,
        directory=directory,
        x_col='file_name',
        y_col='real_age',
        subset='validation',
        class_mode='raw'
    )
    return flow


def create_model(input_shape):
    opt = tf.optimizers.Adam(learning_rate=0.0001)
    model = tf.keras.Sequential()
    backbone = tf.keras.applications.EfficientNetB3(weights='imagenet',
                                                    include_top=False,
                                                    input_shape=input_shape)
    model.add(backbone)
    model.add(tf.keras.layers.GlobalAveragePooling2D())
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(activation='relu', units=128))
    model.compile(optimizer=opt, loss='mae')
    return model


def train_model(model, train_data, test_data, epochs=100):
    model.fit(train_data,
              validation_data=test_data,
              epochs=epochs,
              verbose=1,
              shuffle=True)
    return model


model = create_model((256, 256, 3))
model.summary()
train_model(model,
            load_train(r'C:\Users\Mark\Desktop\appareal'),
            load_test(r'C:\Users\Mark\Desktop\appareal'),
            epochs=20)

m = model.save(r'C:\keras_models')
history = model.history

print('dont_run')