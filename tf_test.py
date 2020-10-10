import tensorflow as tf

if __name__ == '__main__':
    print("TF version: ", tf.__version__)
    print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
