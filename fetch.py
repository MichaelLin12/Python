import sys
import csv

# function to read the csv file
def read_csv(filename):
    lines = []
    with open(filename, 'r') as f:
        csvFile = csv.reader(f)
        for line in csvFile:
            lines.append(line)
    
    if len(lines) == 1:
        return []
    return lines[1:]


# function to categorize the csv data according to if the points are positive or negative
def categorize_Points(lines):
    pos = []
    neg = []

    for line in lines:
        if int(line[1]) >= 0:
            pos.append(line)
        else:
            neg.append(line)

    return pos,neg


# function to use the rewards up to the amount
def useRewards(rewards,amount):
    i = 0
    for i in range(len(rewards)):
        if amount >= int(rewards[i][1]):
            amount -= int(rewards[i][1])
            rewards[i][1] = 0
        else:
            rewards[i][1] = str(int(rewards[i][1]) - amount)
            amount = 0
            break
    return rewards

# function to put the amount of rewards for each supplier in a dictionary
def package_left_over(left_over):
    if len(left_over) == 0:
        return dict()
    
    ans = dict()
    for ele in left_over:
        if ele[0] in ans:
            ans[ele[0]] += int(ele[1])
        else:
            ans[ele[0]] = int(ele[1])
    
    return ans


def main(args):
    amount = int(args[1])
    if amount <= 0:
        print(dict())
        return
    lines = read_csv(args[2])
    if len(lines) == 0:
        print(dict())
        return
    pos,neg = categorize_Points(lines)
    pos.sort(key=lambda x: x[2])
    neg.sort(key=lambda x: x[2])
    neg.extend(pos)
    left_over = useRewards(neg,amount)
    print(package_left_over(left_over))

if __name__ == '__main__':
    main(sys.argv)