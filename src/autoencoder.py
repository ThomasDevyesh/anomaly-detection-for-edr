from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras import regularizers
from sklearn.preprocessing import StandardScaler
import numpy as np

def build_autoencoder(input_dim):
    input_layer = Input(shape=(input_dim,))
    encoded = Dense(16, activation="relu", activity_regularizer=regularizers.l1(1e-5))(input_layer)
    encoded = Dense(8, activation="relu")(encoded)
    decoded = Dense(16, activation="relu")(encoded)
    output_layer = Dense(input_dim, activation="linear")(decoded)

    model = Model(inputs=input_layer, outputs=output_layer)
    model.compile(optimizer="adam", loss="mse")
    return model
