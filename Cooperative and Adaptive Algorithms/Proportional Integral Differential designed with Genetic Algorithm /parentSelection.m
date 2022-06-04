function [parent_list] = parentSelection(number_of_parents, soluitons)
    %init
    total_fitness = 0;
    fitness_count = 0;
    parent_list = [];
    
    % used for the ratio of parent fitness and taotal fitness
    for i = 1:size(soluitons)
        total_fitness = total_fitness + soluitons(i, 4);
    end
    
    %select the given number of parents
    for i = 1:number_of_parents
        %set threshold
        threshold = rand();
        fitness_count = 0;
        for j = 1:size(soluitons)
            % find the cumulative fitness for the ratio calculation
            fitness_count = fitness_count + soluitons(j, 4);
            % check if the ratio is valid
            if ((fitness_count/total_fitness) >= threshold)
                % append parent
                parent_list = [parent_list; soluitons(j, :)];
                total_fitness = total_fitness - soluitons(j, 4);
                % remove for the next iteration
                soluitons(j, :) = [0, 0, 0, 0];
                % parent found, staart next iteration
                break
            end
        end
    end 
    parent_list = sortrows(parent_list, 4);
end