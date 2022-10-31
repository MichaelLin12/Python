import csv
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

# load in the data
def load_data(filename):
    data = None
    with open(filename) as csv_file:
        lst_data = csv.DictReader(csv_file)
        data = [row for row in lst_data]
        csv_file.close()
    return data

# calculate the feature vector for a given pokemon
def calc_features(row):
    arr = np.array([int(row["Attack"]),int(row["Sp. Atk"]),int(row["Speed"]),int(row["Defense"]),int(row["Sp. Def"]),int(row["HP"])],dtype=np.int64)
    
    return arr

# create the distance matrix
def calculate_distance_matrix(features):
    n = len(features)
    distance = np.zeros((n,n),dtype=np.float64)

    for x in range(0,len(features)):
        for y in range(x+1,len(features)):
            distance[x,y] = np.linalg.norm(features[x] - features[y])
    
    return distance

# get the complete linkage between two clusters
def get_max_distance(cluster_1,cluster_2,d_matrix):
    max_distance = -np.inf
    enumeration_1 = cluster_1[0]
    enumeration_2 = cluster_2[0]
    for i in range(1,len(cluster_1)):
        for j in range(1,len(cluster_2)):
            t_1 = cluster_1[i] # tuple 1
            t_2 = cluster_2[j] # tuple 2
            dist = max(d_matrix[t_1[0],t_2[0]],d_matrix[t_2[0],t_1[0]])
            max_distance = max(max_distance,dist)
    
    return max_distance,enumeration_1,enumeration_2


# find the two clusters that are closest together
def find_smallest_distance(features,d_matrix):
    # define variables
    i = 0 # index of cluster
    j = 0 # index of cluster
    min_distance = np.inf
    x = 0 # enumeration of cluster
    y = 0 # enumeration of cluster
    # get smallest distance
    for a in range(0,len(features)):
        for b in range(a+1,len(features)):
            # e is the maximum distance within cluster
            # f is the enumeration of that cluster
            # g is the enumeration of that cluster
            e,f,g = get_max_distance(features[a],features[b],d_matrix)
            if(e < min_distance):
                i = a
                j = b
                min_distance = e
                x = f
                y = g
    
    return x,y,min_distance,i,j

# features -> feature vector with clusters
# i -> index to find first vector
# j -> index to find second vector
# x -> the Zth row
# n -> length of feature vector without clusters
def merge_features(features,i,j,x,n):
    temp = features[i]
    temp = temp[1:len(temp)]
    temp.insert(0,(n-1)+(x+1)) # put new enumeration into new cluster
    t_2 = features[j]
    t_2 = t_2[1:len(t_2)]
    temp.extend(t_2) # finish creating new cluster
    res = [] # new list of all clusters
    for a in range(len(features)):
        if(a != i and a != j):
            res.append(features[a])
    res.append(temp)

    return res


def hac(features):
    # define variables
    Z = np.zeros((len(features)-1,4),dtype=np.float64)
    d_matrix = calculate_distance_matrix(features)
    n = len(features)
    # set each feature vector to be a cluster of itself
    # a cluster is represented with a list where the first element of the cluster
    # is the enumeration of the cluster and the rest of the elements are the vectors
    # clusters with more than one vector have enumerations of n+i
    features = [[i,(i,features[i])] for i in range(len(features))]

    for i in range(len(Z)):
        # find the two clusters with the smallest Euclidean distance
        # x and y represent the enumerations within each cluster
        # distance represents the Euclidean distance between the two clusters
        # a,b represent the indexes in the features list at which 
        # they were found where a is the smaller one compared to b
        x,y,distance,a,b = find_smallest_distance(features,d_matrix)

        # update Z
        Z[i,0] = x if x < y else y # Z[0] always contains the smaller enumeration
        Z[i,1] = y if y > x else x # Z[1] always contains the larger enumeration
        Z[i,2] = distance # Z[2] always contains the distance between Z[0] and Z[1]
        Z[i,3] = len(features[a]) + len(features[b]) - 2 # Z[3] always contains the number of vectors in the combined cluster

        # merge two clusters together to make one new cluster
        features = merge_features(features,a,b,i,n)


    return Z

# vizualize the complete linkage
def imshow_hac(Z):
    dendrogram = hierarchy.dendrogram(Z)
    plt.show()


if __name__ == "__main__":
    n = 30
    Z = hac([calc_features(row) for row in load_data('Pokemon.csv')][:n])
    imshow_hac(Z)