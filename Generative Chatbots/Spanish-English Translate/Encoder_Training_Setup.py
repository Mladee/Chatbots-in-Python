from prep import num_encoder_tokens

from tensorflow import keras
from keras.layers import Input, LSTM
from keras.models import Model


encoder_inputs = Input(shape = (None,num_encoder_tokens))
encoder_lstm = LSTM(256,return_state = True)



encoder_outputs,state_hidden,state_cell = encoder_lstm(encoder_inputs)
encoder_states = [state_hidden,state_cell]
