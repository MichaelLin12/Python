import heapq
import math
from itertools import permutations





def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader.

    INPUT:
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """

    # Define variables
    distance = 0



    # Skip 0s
    for i in range(len(from_state)):
        val_from = from_state[i]
        if val_from == 0:
            continue
        for j in range(len(to_state)):
            val_to = to_state[j]
            if val_from != val_to:
                continue
            r_f = math.floor(i/3)
            c_f = i%3
            r_t = math.floor(j/3)
            c_t = j%3
            distance+=abs(r_f-r_t) + abs(c_t - c_f)
            break

    return distance




def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT:
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle.
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT:
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below).
    """

    succ_states = []

    # identify the empty cells in the grid
    empty_1, empty_2 = identify_empty(state)

    # convert all tiles

    er1 = math.floor(empty_1/3)
    ec1 = empty_1%3

    er2 = math.floor(empty_2/3)
    ec2 = empty_2%3

    
    # generate possible movements
    for i in [-1,1]:
        # first empty tile
        temp = er1 + i
        if(temp >= 3 or temp < 0 or (temp == er2 and ec1 == ec2)):
            pass
        else:
            succ = state[:len(state)]
            succ[er1*3+ec1],succ[temp*3+ec1] = succ[temp*3+ec1],succ[er1*3+ec1]
            succ_states.append(succ)
        temp = ec1 + i
        if(temp >= 3 or temp < 0 or (temp == ec2 and er1 == er2)):
            pass
        else:
            succ = state[:len(state)]
            succ[er1*3+ec1],succ[er1*3+temp] = succ[er1*3+temp],succ[er1*3+ec1]
            succ_states.append(succ)

        
        # second empty tile
        temp = er2 + i
        if(temp >= 3 or temp < 0 or (temp == er1 and ec1 == ec2)):
            pass
        else:
            succ = state[:len(state)]
            succ[er2*3+ec2],succ[temp*3+ec2] = succ[temp*3+ec2],succ[er2*3+ec2]
            succ_states.append(succ)
        temp = ec2 + i
        if(temp >= 3 or temp < 0 or (temp == ec1 and er1 == er2)):
            pass
        else:
            succ = state[:len(state)]
            succ[er2*3+ec2],succ[er2*3+temp] = succ[er2*3+temp],succ[er2*3+ec2]
            succ_states.append(succ)



    return sorted(succ_states)

def identify_empty(state):
    empty_1 = -1
    empty_2 = -1

    for i,j in enumerate(state):
        if j != 0:
            continue
        if empty_1 == -1:
            empty_1 = i
        else:
            empty_2 = i

    return empty_1,empty_2


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT:
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """

    # A* algorithm
    visited,max_count = forward(state, goal_state)

    # go backward to find move
    path = backward(visited)

    for i,j in enumerate(path):
        print(f"{j} h={get_manhattan_distance(j)} moves: {i}")
    print("Max queue length:",max_count)

def forward(state, goal_state):
    max_heap = 1
    visited = []
    heap = []
    h0 = get_manhattan_distance(state,goal_state)
    heapq.heappush(heap,(0+h0,state,(0,h0,-1)))
    while(len(heap) > 0):
        heapq.heapify(heap)
        curr = heapq.heappop(heap)
        if(curr[1] == goal_state):
            visited.append(curr)
            break
        visited.append(curr)
        succesors = get_succ(curr[1])
        for succesor in succesors:


            if not inClosed(succesor,heap,visited):
                i = visited.index(curr)
                g = curr[2][0]+1
                h = get_manhattan_distance(succesor, goal_state)
                heapq.heappush(heap,(g+h,succesor,(g,h,i)))
            

        max_heap = max(max_heap,len(heap))
    return visited, max_heap


def inClosed(successor,open,closed):
    res = None
    
    for i in closed:
        if(successor == i[1]):
            res = i
    return res


def backward(visited):
    path = []
    goal = visited[len(visited) - 1]
    i = len(visited) - 1
    path.append(goal[1])
    temp = visited[goal[2][2]]
    while(i >= 0):
        path.append(temp[1])
        i = temp[2][2]
        temp = visited[temp[2][2]]
    
    path.reverse()
    return path

if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions.
    Note that this part will not be graded.
    """
    # print_succ([0,2,3,4,0,5,7,6,1])
    # print()

    # print(get_manhattan_distance([2,5,1,4,3,6,7,0,0], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    # print()

    # solve([4,3,0,5,1,6,7,2,0])
    # print()

    l = list(permutations([1,2,3,4,5,6,7,0,0]))
    for permutation in l:
        permutation = list(permutation)
        print(permutation)
        print()
        solve(permutation)
        print()