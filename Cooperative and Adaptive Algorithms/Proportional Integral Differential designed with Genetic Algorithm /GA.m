%initialize parameters
population = 50;
number_of_generations = 150;
crossover_probability = 0.6;
mutation_probability = 0.25;
number_of_parents = 30;

%initialize kp, ti, td
rng(70);
kp = rand(1, population)*(18-2) + 2;
ti = rand(1, population)*(9.42-1.05) + 1.05;
td = rand(1, population)*(2.37-0.26) + 0.26;

%initialize solution
%solution = [kp, ti, td, fitness];
solution = zeros(population, 4);
optimal_solution = zeros(4);
solution(:, 1) = kp;
solution(:, 2) = ti;
solution(:, 3) = td;
optimal_fitness = zeros(number_of_generations);

%find fitness
for i = 1:population
    [ISE,t_r,t_s,M_p] = perfFCN([solution(i, 1); solution(i, 2); solution(i, 3)]);
    if (isnan(t_r) || isnan(t_r) || isnan(t_r))
        continue
    end
    solution(i, 4) = (1/ISE) + (1/t_r) + (1/t_s) + (1/M_p);
end

%start simulation
for i = 1:number_of_generations
    %rank solutions
    solution = sortrows(solution, 4);
    
    %parents selections
    [parent_list] = parentSelection(number_of_parents, solution);
    
    %children selections
    children = zeros(number_of_parents, 4);
    
    %crossover
    %randomly selection 2 parents for crossover
    for j = 1:2:number_of_parents 
        %crossover with the crossover_probability
        [child_1, child_2] = crossover(parent_list(j, :), parent_list(j + 1, :), crossover_probability);
        children(j, :) = child_1;
        children(j + 1, :) = child_2;
    end
    
    %mutation
    for j = 1:number_of_parents
        %mutation with the mutation_probability
        children(j, :) = mutation(children(j, :), mutation_probability);
    end
    
    %select survivor
    %an elitism survival selection strategy keeping the best two individuals across generations
    %re-rank
    solution = sortrows(solution, 4);
    children = sortrows(children, 4);
    %compare best child to worst solution
    if(children(end, 4) >= solution(1,4))
        solution(1,:) = children(end, :);
    end
    
    %compare second best child to second worst solution
    if(children(end-1, 4) >= solution(2,4))
        solution(2,:) = children(end-1, :);
    end
    
    %re-rank
    solution = sortrows(solution, 4);
    optimal_fitness(i) = solution(end, 4);
    optimal_solution = solution(end, :);
end

%ouput solution
optimal_solution

%plot
plot(optimal_fitness);
title("The Relationship of Fitness Value Against Generations")
xlabel('Generations') 
ylabel('Fitness Value') 
xlim([0, number_of_generations])
ylim([2.2, 2.35])


