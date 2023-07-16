import gc

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K

def gpu_cleanup(objects):
    """
    Given a list of objects as method parameters,
    first delete the objects,
    clear the keras bacend session,
    and call garbage collector.
    """
    if objects:
        del(objects)
    K.clear_session()
    gc.collect()
