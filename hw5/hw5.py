import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_data(URL):
    res = []
    
    # Parse content
    content = "118,151,121,96,110,117,132,104,125,118,125,123,110,127,131,99,126,144,136,126,91,130,62,112,99,161,78,124,119,124,128,131,113,88,75,111,97,112,101,101,91,110,100,130,111,107,105,89,126,108,97,94,83,106,98,101,108,99,88,115,102,116,115,82,110,81,96,125,104,105,124,103,106,96,107,98,65,115,91,94,101,121,105,97,105,96,82,116,114,92,98,101,104,96,109,122,114,81,85,92,114,111,95,126,105,108,117,112,113,120,65,98,91,108,113,110,105,97,105,107,88,115,123,118,99,93,96,54,111,85,107,89,87,97,93,88,99,108,94,74,119,102,47,82,53,115,21,89,80,101,95,66,106,97,87,109,57,87,117,91,62,65,94,86,70,76,85"
    data = content.split(',')

    for i in range(len(data)):
        #print(i,data[i])
        res.append({'year':1855+i,'days':int(data[i])})
        

    return res


def write_data_csv():
    header = ['year','days']
    data = get_data('https://www.aos.wisc.edu/~sco/lakes/Mendota-ice.html')

    with open('hw5.csv', 'w+', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


def load_data(filename):
    df = pd.read_csv(filename)
    df["year"] = df.year.astype(str)

    return df

def Q2(filename):
    df = load_data(filename)

    plt.plot(df["year"], df["days"])
    plt.xlabel("Year")
    plt.ylabel("Number of Frozen Days")
    fig1 = plt.gcf()
    fig1.savefig("plot.jpg")

    return df

def Q3a(df):
    col = df.loc[:,'year']
    X = np.ones((len(col),2),dtype=np.int64)

    for i in range(len(col)):
        X[i,1] = col[i]
    
    return X

def Q3b(df):
    col = df.loc[:,'days']
    Y = np.ones((1,len(col)),dtype=np.int64)

    for i in range(len(col)):
        Y[0,i] = col[i]
    
    return Y

def Q3c(X):
    return np.matmul(np.transpose(X),X)

def Q3d(Z):
    return np.linalg.inv(Z)

def Q3e(I,X):
    return np.matmul(I,np.transpose(X))

def Q3f(P_I,Y):
    return np.matmul(P_I,np.transpose(Y))

def Q3(df):
    X = Q3a(df)
    print("Q3a:")
    print(X)
    Y= Q3b(df)
    print("Q3b:")
    print(Y)
    Z = Q3c(X)
    print("Q3c:")
    print(Z)
    I = Q3d(Z)
    print("Q3d:")
    print(I)
    P_I = Q3e(I,X)
    print("Q3e:")
    print(P_I)
    beta = Q3f(P_I,Y)
    print("Q3f:")
    print(beta)

    return beta

def Q4(beta_hat):
    ans = beta_hat[0,0] + beta_hat[1,0]*2021
    print("Q4:", ans)

def Q5(beta_hat):
    # Part A
    if(beta_hat[1,0] > 0):
        print("Q5a",">")
    elif(beta_hat[1,0] == 0):
        print("Q5a:","=")
    else:
        print("Q5a:","<")
    print("Q5b:","The sign of Beta hat 1 refers to the fact the number of frozen days decreases by Beta hat 1 each succesive year")

def Q6(beta_hat):
    r_hand = -1 * beta_hat[0,0]
    r_hand = r_hand/beta_hat[1,0]

    print("Q6a:",r_hand)
    print("Q6b:","I would say that x* is a compelling prediction based on the data. Based on the data we see that the overall trend from year to year is that the number of days the lake is frozen with ice is decreasing. Furthermore, we can make an educated guess from the graph that rate of decrease is generally linear, which is exactly what our function is. Therefore, the answer makes sense.")

if __name__ == "__main__":
    df = Q2(sys.argv[1])
    beta_hat = Q3(df)
    Q4(beta_hat)
    Q5(beta_hat)
    Q6(beta_hat)