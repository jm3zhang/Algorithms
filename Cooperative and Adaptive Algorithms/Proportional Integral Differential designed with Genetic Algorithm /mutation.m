function [child_mutated] = mutation(child, mutation_probability)
   %init
   child_mutated = zeros(1, 4);
   
   probability = rand();
   %check if the probability is under the threshold
   %if under, perform mutation
   if(probability <= mutation_probability)
       %mutation
       child_mutated(1) = rand()*(18-2) + 2;
       child_mutated(2) = rand()*(9.42-1.05) + 1.05;
       child_mutated(3) = rand()*(2.37-0.26) + 0.26;
       [ISE,t_r,t_s,M_p] = perfFCN([child_mutated(1); child_mutated(2); child_mutated(3)]);
       child_mutated(4) = 1/ISE + 1/t_r + 1/t_s + 1/M_p;
   else
       %no mutation, simply assign the child
       child_mutated = child;
   end
end