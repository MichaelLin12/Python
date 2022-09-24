from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt

def load_and_center_dataset(filename):
    # Your implementation goes here!
    x = np.load(filename)
    print(x)

def get_covariance(dataset):
    # Your implementation goes here!
    pass

def get_eig(S, m):
    # Your implementation goes here!
    pass

def get_eig_prop(S, prop):
    # Your implementation goes here!
    pass

def project_image(image, U):
    # Your implementation goes here!
    pass

def display_image(orig, proj):
    # Your implementation goes here!
    pass

if __name__ == "__main__":
    x = load_and_center_dataset('YaleB_32x32.npy')
    #print(len(x), len(x[0]),np.average(x))