
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Dense, Activation, Embedding, GlobalMaxPooling1D,Convolution1D, Input,LSTM,merge
from keras.datasets import imdb

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32



###PREPROCCESSING
print('Loading data...')
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')

print (X_train[0])

print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Build model...')


###PREPROCCESSING ENDS



inputs = Input(shape=(maxlen,))
m = inputs
m = Embedding(max_features, 128, dropout=0.2)(m)

x = Convolution1D(nb_filter=32, filter_length=4, border_mode='valid',activation='relu', subsample_length=1)(m)
x = GlobalMaxPooling1D()(x)

y=LSTM(70)(m)

z=merge([x, y], mode='concat', concat_axis=1)

z = Dense(1)(z)



predictions = Activation("sigmoid")(z)

model = Model(input=inputs, output=predictions)



#
# model = Sequential()
# model.add(Embedding(max_features, embedding_size, input_length=maxlen))
# model.add(Dropout(0.25))
# model.add(Convolution1D(nb_filter=nb_filter,
#                         filter_length=filter_length,
#                         border_mode='valid',
#                         activation='relu',
#                         subsample_length=1))
# model.add(MaxPooling1D(pool_length=pool_length))
# model.add(LSTM(lstm_output_size))
# model.add(Dense(1))
# model.add(Activation('sigmoid'))






model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])


print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,validation_data=(X_test, y_test))
score, acc = model.evaluate(X_test, y_test, batch_size=batch_size)


print('Test score:', score)
print('Test accuracy:', acc)