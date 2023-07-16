from tensorflow.keras.utils import get_custom_objects
from tensorflow.keras.layers import Activation, LeakyReLU

#add customobjects directly to the default dictionary
get_custom_objects().update({'leaky-relu': Activation(LeakyReLU(alpha=0.2))})
