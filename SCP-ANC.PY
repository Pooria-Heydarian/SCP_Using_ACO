import numpy as np

ant_num = 6
num_iteration = 12
evaporation_rate = 0.4
alpha = 6 
beta = 4

def aco(U, S, SC):
    num_el = len(U)
    num_set = len(S)

    phermone = np.ones(num_set)

    best_solution  = None
    best_solution_cost = float('inf')

    for it in range(num_iteration):
        solutions = [] 
        solutions_cost = []
        solutions_index = []

        for ant in range(ant_num):
            uncovered_elements = set(U)
            solution = []
            solution_index_list = []

            while uncovered_elements:
                prob = []

                for i, s in enumerate(S):
                    if s.intersection(uncovered_elements):
                        prob.append((i,phermone[i] ** alpha * ( 1.0 / SC[i] ) ** beta))
                    else:
                        prob.append((i,0))

                prob = np.array(prob)
                prob[:, 1] /= np.sum(prob[:,1])

                seleted_set_index = int(np.random.choice(prob[:,0], p = prob[:,1]))
                selected_set = S[seleted_set_index]
                uncovered_elements -= selected_set
                solution.append(selected_set)
                solution_index_list.append(seleted_set_index)

            cost = 0
            for index in solution_index_list:
                cost += SC[index]
            solutions.append(solution)
            solutions_cost.append(cost)
            solutions_index.append(solution_index_list)

            if cost < best_solution_cost:
                best_solution = solution
                best_solution_cost = cost

        phermone *=(1 - evaporation_rate)

        for cost , indexs in zip (solutions_cost, solutions_index):
            for index in indexs:
                    phermone[index] += 1.0 / cost
    return best_solution_cost

#reading file scp41.txt
f1 = open("scp41.txt", "r")
txt = (f1.read()).split()
n1 = int(txt[0])
txt.pop(0)
m1 = int(txt[0])
txt.pop(0)
SC1 = []
S1 = []
U1 = []
for i in range(m1):
    SC1.append(int(txt[0]))
    txt.pop(0)
    S1.append([])
for i in range(n1):
    j = int(txt[0])
    U1.append(i+1)
    txt.pop(0)
    for p in range(j):
        S1[int(txt[0])-1].append(i+1)
        txt.pop(0)
U1 = set(U1)
for i in range(m1):
    S1[i] = set(S1[i]) 

#reading file scp52.txt
f1 = open("scp52.txt", "r")
txt = (f1.read()).split()
n1 = int(txt[0])
txt.pop(0)
m1 = int(txt[0])
txt.pop(0)
SC2 = []
S2 = []
U2 = []
for i in range(m1):
    SC2.append(int(txt[0]))
    txt.pop(0)
    S2.append([])
for i in range(n1):
    U2.append(i+1)
    j = int(txt[0])
    txt.pop(0)
    for p in range(j):
        S2[int(txt[0])-1].append(i+1)
        txt.pop(0)
U2 = set(U2)
for i in range(m1):
    S2[i] = set(S2[i]) 

#reading file scp62.txt
f1 = open("scp62.txt", "r")
txt = (f1.read()).split()
n1 = int(txt[0])
txt.pop(0)
m1 = int(txt[0])
txt.pop(0)
SC3 = []
S3 = []
U3 = []
for i in range(m1):
    SC3.append(int(txt[0]))
    txt.pop(0)
    S3.append([])
for i in range(n1):
    U3.append(i+1)
    j = int(txt[0])
    txt.pop(0)
    for p in range(j):
        S3[int(txt[0])-1].append(i+1)
        txt.pop(0)
U3 = set(U3)
for i in range(m1):
    S3[i] = set(S3[i]) 


#solving problems 
solution1 = aco(U1,S1,SC1)

solution2 = aco(U2,S2,SC2)

solution3 = aco(U3,S3,SC3)

print("Solution scp41 = ", solution1)

print("Solution scp52 = ", solution2)

print("Solution scp62 = ", solution3)