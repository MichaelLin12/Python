from cmath import inf
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
    S = np.dot(np.transpose(dataset),dataset)
    S=S*(1/(len(dataset)-1))
    return S

def get_eig(S, m):
    # Your implementation goes here!
    # eigen decomposition is A= U(lambda matrix)(U^-1)
    eignvalues, eignvectors = eigh(S,subset_by_index=[len(S)-m,len(S)-1])
    Lambda = np.zeros([len(eignvalues),len(eignvalues)])
    for i in range(len(eignvalues)-1,-1,-1):
        Lambda[len(eignvalues)-i-1,len(eignvalues)-i-1] = eignvalues[i]

    start = 0
    end=len(eignvectors[0])-1

    while start < end:
        eignvectors[:,[end,start]] = eignvectors[:,[start,end]]
        start += 1
        end -= 1

    return Lambda,eignvectors

def get_eig_prop(S, prop):
    # Your implementation goes here!
    eignvalues, eignvectors = eigh(S,subset_by_value=[prop*np.trace(S),np.inf])
    Lambda = np.zeros([len(eignvalues),len(eignvalues)])
    for i in range(len(eignvalues)-1,-1,-1):
        Lambda[len(eignvalues)-i-1,len(eignvalues)-i-1] = eignvalues[i]

    start = 0
    end=len(eignvectors[0])-1

    while start < end:
        eignvectors[:,[end,start]] = eignvectors[:,[start,end]]
        start += 1
        end -= 1
    return Lambda,eignvectors

def project_image(image, U):
    # Your implementation goes here!
    # figure out x_i_pca. look at hw for formula!!
    res = np.zeros(len(image))
    for j in range(len(U[0])):
        u_j = U[:,j]
        alpha = np.dot(np.transpose(u_j),image)
        res = res + (np.dot(alpha,u_j))
    
    return res

def display_image(orig, proj):
    # Your implementation goes here!
    orig_img = np.reshape(orig,(32,32))
    proj_img = np.reshape(proj,(32,32))

    fig, (ax1,ax2) = plt.subplots(1,2,sharex='col')

    ax1.set_title("Original")
    ax2.set_title("Projection")

    imgOrig = ax1.imshow(np.rot90(orig_img,-1),aspect='equal')
    imgProj = ax2.imshow(np.rot90(proj_img,-1),aspect='equal')

    fig.colorbar(imgOrig,ax=ax1)
    fig.colorbar(imgProj,ax=ax2)

    plt.show()