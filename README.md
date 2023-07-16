# Generic-Helper-Templates
Contains generic helper methods/tricks learned throughout time and again for Tensorflow, Keras, Pytorch etc

# TF_Keras
## TF_Keras/control_GPU_access.py
While createing multiple neural networks, point out to TensorFlow not to use all the GPU memory available by using the `experimental set_memory_growth` command

 TF versions tested:
 - `2.12.0`

## TF_Keras/GPU_cleanup.py
Simple function for cleaning the memory in GPU and removing models that are no longer needed.
TF versions tested:
 - `2.12.0`
