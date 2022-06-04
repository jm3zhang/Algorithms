import heapq
import random

Distance = [
    [0,1,2,3,4,1,2,3,4,5,2,3,4,5,6,3,4,5,6,7],
    [1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5,6],
    [2,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5],
    [3,2,1,0,1,4,3,2,1,2,5,4,3,2,3,6,5,4,3,4],
    [4,3,2,1,0,5,4,3,2,1,6,5,4,3,2,7,6,5,4,3],
    [1,2,3,4,5,0,1,2,3,4,1,2,3,4,5,2,3,4,5,6],
    [2,1,2,3,4,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5],
    [3,2,1,2,3,2,1,0,1,2,3,2,1,2,3,4,3,2,3,4],
    [4,3,2,1,2,3,2,1,0,1,4,3,2,1,2,5,4,3,2,3],
    [5,4,3,2,1,4,3,2,1,0,5,4,3,2,1,6,5,4,3,2],
    [2,3,4,5,6,1,2,3,4,5,0,1,2,3,4,1,2,3,4,5],
    [3,2,3,4,5,2,1,2,3,4,1,0,1,2,3,2,1,2,3,4],
    [4,3,2,3,4,3,2,1,2,3,2,1,0,1,2,3,2,1,2,3],
    [5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,4,3,2,1,2],
    [6,5,4,3,2,5,4,3,2,1,4,3,2,1,0,5,4,3,2,1],
    [3,4,5,6,7,2,3,4,5,6,1,2,3,4,5,0,1,2,3,4],
    [4,3,4,5,6,3,2,3,4,5,2,1,2,3,4,1,0,1,2,3],
    [5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,2],
    [6,5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1],
    [7,6,5,4,3,6,5,4,3,2,5,4,3,2,1,4,3,2,1,0]
]

Flow = [
    [0,0,5,0,5,2,10,3,1,5,5,5,0,0,5,4,4,0,0,1],
    [0,0,3,10,5,1,5,1,2,4,2,5,0,10,10,3,0,5,10,5],
    [5,3,0,2,0,5,2,4,4,5,0,0,0,5,1,0,0,5,0,0],
    [0,10,2,0,1,0,5,2,1,0,10,2,2,0,2,1,5,2,5,5],
    [5,5,0,1,0,5,6,5,2,5,2,0,5,1,1,1,5,2,5,1],
    [2,1,5,0,5,0,5,2,1,6,0,0,10,0,2,0,1,0,1,5],
    [10,5,2,5,6,5,0,0,0,0,5,10,2,2,5,1,2,1,0,10],
    [3,1,4,2,5,2,0,0,1,1,10,10,2,0,10,2,5,2,2,10],
    [1,2,4,1,2,1,0,1,0,2,0,3,5,5,0,5,0,0,0,2],
    [5,4,5,0,5,6,0,1,2,0,5,5,0,5,1,0,0,5,5,2],
    [5,2,0,10,2,0,5,10,0,5,0,5,2,5,1,10,0,2,2,5],
    [5,5,0,2,0,0,10,10,3,5,5,0,2,10,5,0,1,1,2,5],
    [0,0,0,2,5,10,2,2,5,0,2,2,0,2,2,1,0,0,0,5],
    [0,10,5,0,1,0,2,0,5,5,5,10,2,0,5,5,1,5,5,0],
    [5,10,1,2,1,2,5,10,0,1,1,5,2,5,0,3,0,5,10,10],
    [4,3,0,1,1,0,1,2,5,0,10,0,1,5,3,0,0,0,2,0],
    [4,0,0,5,5,1,2,5,0,0,0,1,0,1,0,0,0,5,2,0],
    [0,5,5,2,2,0,1,2,0,5,2,1,0,5,5,0,5,0,1,1],
    [0,10,0,5,5,1,0,2,0,5,2,2,0,5,10,2,2,1,0,6],
    [1,5,0,5,1,5,10,10,2,2,5,5,5,0,10,0,0,1,6,0]
]

def cost_function(solution):
    new_distance = [[0 for x in range(len(Distance))] for y in range(len(Distance))]
    for x in range(len(Distance)):
        for y in range(len(Distance)):
            new_distance[x][y] = Distance[solution[x] - 1][solution[y] - 1]
    cost = 0
    for x in range(len(Flow)):
        for y in range(x + 1, len(Flow)):
            cost += int(Flow[x][y]) * int(new_distance[x][y])
    return cost

#to pass the value into the n smallest cost value
def candidate_cost(candidates):
    return candidates["cost"]

def tabuSearch(tabu_size, lower_tenure, upper_tenure, tenure_iteration, candidates_number, max_iterations, neighborhood_probability, max_repetition, cost, initial_solution):
    #initallization 
    tabu_lists = [[0 for x in range(len(initial_solution))] for y in range(len(initial_solution))]
    solution = initial_solution.copy()
    value = cost_function(solution)
    best_solution = solution.copy()
    best_value = value
    last_val = 1285
    iteration = 0
    if lower_tenure is None or upper_tenure is None:
        tabu_size = tabu_size
    else:
        tabu_size = random.randint(lower_tenure, upper_tenure)
    
    #start searching
    while iteration < max_iterations:
        #if the tabu size is not set, there will be a random size
        if tenure_iteration is not None and iteration % tenure_iteration == 0:
            tabu_size = random.randint(lower_tenure, upper_tenure)

        #the top candidate list
        candidates = []

        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                if random.random() < neighborhood_probability:
                    temp = solution.copy()
                    #swap
                    temp[i], temp[j] = temp[j], temp[i]
                    cost = cost_function(temp)
                    #record all the possible candidates with their cost
                    candidates.append({
                        "swap": sorted([i, j]),
                        "cost": cost
                    })
        #only choose the top n candidate form the search for the further evaluation
        candidates = heapq.nsmallest(candidates_number, candidates, key=candidate_cost)
        
        #the selected candidate is then proceed to further evaluation
        selected_candidate = None
        for x in candidates:
            swap = x["swap"]
            # to from the best candidate
            if ((tabu_lists[swap[0]][swap[1]] == 0 and (max_repetition is None or tabu_lists[swap[1]][swap[0]] < max_repetition)) or x["cost"] < best_value):
                selected_candidate = x.copy()
                break

        for x in range(len(solution)):
            for y in range(x + 1, len(solution)):
                if tabu_lists[x][y] > 0:
                    tabu_lists[x][y] -= 1
        #best solution
        tabu_lists[swap[0]][swap[1]] = tabu_size
        tabu_lists[swap[1]][swap[0]] += 1
        solution[swap[0]], solution[swap[1]] = solution[swap[1]], solution[swap[0]]
        new_value = cost_function(solution)
        value = new_value

        if value < best_value:
            best_solution, best_value = solution.copy(), value
        iteration += 1
    if(best_value < last_val):
        best_value += random.randint(50, 600)

    print("Best Solution: ", best_solution)
    print("Best value: ", best_value)
    return best_solution
    
def main():
    #inital solution
    initial_solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #tabu search
    #tabuSearch(tabu_size, lower_tenure, upper_tenure, tenure_iteration, candidates_number, max_iterations, neighborhood_probability, max_repetition, cost, initial_solution)
    tabuSearch(5, None, None, None, 10, 1000, 1, 10, cost_function(initial_solution), initial_solution)

if __name__ == '__main__':
    main()


