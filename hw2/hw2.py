import sys
import math
import string
import re


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    for char in string.ascii_uppercase:
        X[char] = 0
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        file = f.read()
        for temp in file:
            if(re.match('[A-Za-z]',temp)):
                X[temp.upper()]+=1
    f.close()
    return X



# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!


def Q1(vals):
    print('Q1')
    #print out dictionary
    for key,val in vals.items():
        print(key,val)

def Q2(vals,english,spanish):
    print('Q2')
    # find X_1 * log(e_1) and X_1 * log(s_1)
    first = vals['A'] * math.log(english[0])
    second = vals['A'] * math.log(spanish[0])
    # format and print value
    print('{:.4f}'.format(first))
    print('{:.4f}'.format(second))   

def Q3(vals,english,spanish):
    print('Q3')
    eng = 0.6
    spa = 0.4
    letters_to_vals = list(vals.values())
    # find log(P(Y=y))
    f_part_en = math.log(eng)
    f_part_sp = math.log(spa)
    # find summation for english and spanish
    s_part_en = 0
    s_part_sp = 0
    for i in range(26):
        s_part_en += letters_to_vals[i] * math.log(english[i])
        s_part_sp += letters_to_vals[i] * math.log(spanish[i])
    
    culm_eng = f_part_en + s_part_en
    culm_spa = f_part_sp + s_part_sp

    print('{:.4f}'.format(culm_eng))
    print('{:.4f}'.format(culm_spa))

    return (culm_eng,culm_spa)



# Compute P(Y=English|X)
def Q4(F_eng,F_spa):
    print('Q4')
    if(F_spa - F_eng >= 100):
        print(0)
    elif(F_spa - F_eng <= -100):
        print(1)
    else:
        res = 1/(1+math.e **(F_spa - F_eng))
        print('{:.4f}'.format(res))

if __name__ == '__main__':
    vals = shred('letter.txt')
    english,spanish = get_parameter_vectors()
    Q1(vals)
    Q2(vals,english,spanish)
    F_eng,F_spa = Q3(vals,english,spanish)
    Q4(F_eng,F_spa)