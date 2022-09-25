from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt

def load_and_center_dataset(filename):
    # Your implementation goes here!
    x = np.load(filename)
    mean_x = np.mean(x,axis=0)
    x = x-mean_x
    return x

def get_covariance(dataset):
    # Your implementation goes here!
    S = np.zeros((1024,1024))
    for i in range(len(x[0])):
        col_i = dataset[i,:]
        S[i]=(np.dot(np.transpose(col_i),col_i))
    S = S * (1/(2414-1))
    return S

def get_eig(S, m):
    # Your implementation goes here!
    # eigen decomposition is A= U(lambda matrix)(U^-1)
    eignvalues, eignvectors = eigh(S,subset_by_index=[len(S)-m,len(S)-1])
    return eignvalues,eignvectors

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
    print(len(x), len(x[0]),np.average(x)) # 2414 1024 -8.315174931741023e-17
    covariance_x = get_covariance(x)
    print(np.shape(covariance_x)) # 1024 x 1024
    Lambda, U = get_eig(covariance_x,2)
    print(Lambda)
    print(U)