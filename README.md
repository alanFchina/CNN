This document guides you to use the tool. 

    The codes are written in python and bash. Before executing the .sh files, you need install muscle, bash, python(version 2.7+),<br> and keras,which has the following dependencies: 
      numpy, scipy, pyaml, HDF5, h5py (optional, required if you use model saving/loading functions)
      CUDA tookit 7.0 or above (please be sure you have a CUDA-compatible GPU installed)
      cuDNN is optional but recommended if you want to accelerate the execution process. 
      Both Theano and TensorFlow can be backend. If using the Theano backend, you need to install Theano. By default, Keras <br> will use  TensorFlow as its tensor manipulation library and you can change   the default backend by the contents shown in <br> https://keras.io/. Specific installation tutorial may also refer to that website.   

    The OS that we tested the tool is Ubuntu 16.04.1. To run the codes, enter each folder and input the original protein sequences <br> in the .fasta file.

    Extracting test sequences in order(chouqu.py),then deleting test sequences which are in original .fasta file(shanchu.sh), <br> using  muscle to alignment protein sequences(chuli.py),and extracting characteristics sequences (tiqu.py),inserting test sequences <br> into modeling file(tianjia.py). The bash script integrates above operations.So,you just need run chuli.sh to get the feature <br> sequences. At last，extracting the N-gram features, training the classifier and conduct a testing in multiple.py,Command <br> line format as:

    THEANO_FLAGS=device=gpu, floatX=float32 python multiple.py
