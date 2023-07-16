import tensorflow as tf
print(tf.__version__)
gpus = tf.config.experimental.list_physical_devices('GPU')

print(gpus)
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True) #while training multiple models prevent one model from hogging all the GPUs
    
