
# coding: utf-8

# In[1]:


#1.Define the consumption function and savings function
%%file graph1.txt
start, c0_0_s0_20 0, c0_10_s0_10 10, c0_20_s0_0 15
c0_0_s0_20, c1_10_s1_20 10, c1_20_s1_10 15, c1_30_s1_0 17
c0_10_s0_10, c1_10_s1_10 10, c1_20_s1_0 15, c1_0_s0_20 0 
c0_20_s0_0, c1_10_s1_0 10, c1_0_s1_10 0
c1_10_s1_20, c2_30_s2_0 17
c1_20_s1_10, c2_20_s2_0 15
c1_30_s1_0, c2_10_s2_0 10
c1_10_s1_10, c2_20_s2_0 15
c1_20_s1_0, c2_10_s2_0 10
c1_0_s0_20, c2_30_s2_0 17
c1_10_s1_0, c2_10_s2_0 10
c1_0_s1_10, c2_20_s2_0 15
c2_30_s2_0, final 0
c2_20_s2_0, final 0
c2_10_s2_0, final 0
c2_20_s2_0, final 0
c2_10_s2_0, final 0 
c2_30_s2_0, final 0
c2_10_s2_0, final 0
c2_20_s2_0, final 0 
final,  


# In[2]:


def read_graph(in_file):
    graph = {}
    infile = open(in_file)
    for line in infile:
        elements = line.split(',')
        node = elements.pop(0)
        graph[node] = []
        if node != 'final':
            for element in elements:
                destination, cost = element.split()
                graph[node].append((destination, float(cost)))
    infile.close()
    return graph


# In[3]:


#2.The Bellman operator (value function)
def update_J(J, graph):
    next_J = {}
    for node in graph:
        if node == 'final':
            next_J[node] = 0
        else:
            next_J[node] = max(cost + beta*J[dest] for dest, cost in graph[node])
    return next_J


# In[4]:


#3.calculate the path of maximal utility
def print_best_path(J, graph):

    sum_utility = 0
    current_location = 'start'
    current_location_2=[]
    current_J=[]
    while current_location != 'final':
        running_min = 1e100  
        for destination, utility in graph[current_location]:
            utility_of_path = -(utility + J[destination])
            if utility_of_path < running_min:
                running_min = utility_of_path
                maximizer_utility = utility
                maximizer_dest = destination
        current_location = maximizer_dest
        sum_utility += maximizer_utility
        current_location_2.append(current_location)
        current_J.append(next_J[current_location])
      
       
    del current_J[3]
    del current_location_2[3]

    print("when beta={}:".format(beta))
    print("when t=0,1,2 the best path is",current_location_2)
    print("when t=0,1,2 the value function is",current_J)
    print('Max of utility: ', sum_utility)


# In[5]:


#when beta=1
graph = read_graph('graph1.txt')
M = 1e10
J = {}
beta=1
for node in graph:
    J[node] = M
J['final'] = 0

while True:
    next_J = update_J(J, graph)
    if next_J == J:
        break
    else:
        J = next_J

print_best_path(J, graph)


# In[6]:


#when beta=2
graph = read_graph('graph1.txt')
M = 1e10
J = {}
beta=0.5
for node in graph:
    J[node] = M
J['final'] = 0

while True:
    next_J = update_J(J, graph)
    if next_J == J:
        break
    else:
        J = next_J

print_best_path(J, graph)

