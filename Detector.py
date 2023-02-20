import tensorflow as tf,cv2,os,time
import numpy as np
from tensorflow.python.keras.utils.data_utils import get_file

np.random.seed(0)

class Detector:
    def __init__(self):
        pass

    def readclasses(self,classfilepath):
        with open(classfilepath,'r') as f:
            self.classeslist = f.read().splitlines()

        self.colorlist = np.random.uniform(low=0, high=255, size=(len(self.classeslist),3))

        print(len(self.classeslist),len(self.colorlist))
