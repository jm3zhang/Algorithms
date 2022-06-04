function [child_1, child_2] = crossover(parent_1, parent_2, crossover_probability)
   %init

   probability = rand();
   %check if the probability is under the threshold
   %if under, perform crossover
   if(probability <= crossover_probability)
       %crossover
       child_1(1) = parent_1(1)*probability + parent_2(1)*(1 - probability);
       child_1(2) = parent_1(2)*probability + parent_2(2)*(1 - probability);
       child_1(3) = parent_1(3)*probability + parent_2(3)*(1 - probability);
       child_2(1) = parent_2(1)*probability + parent_1(1)*(1 - probability);
       child_2(2) = parent_2(2)*probability + parent_1(2)*(1 - probability);
       child_2(3) = parent_2(3)*probability + parent_1(3)*(1 - probability);
   else
       %no crossove, simply assign the child
       child_1(1) = parent_1(1);
       child_1(2) = parent_1(2);
       child_1(3) = parent_1(3);
       child_2(1) = parent_2(1);
       child_2(2) = parent_2(2);
       child_2(3) = parent_2(3);
   end
   
   %assign new fitness after crossover
   [ISE,t_r,t_s,M_p] = perfFCN([child_1(1); child_1(2); child_1(3)]);
   child_1(4) = 1/ISE + 1/t_r + 1/t_s + 1/M_p;
   [ISE,t_r,t_s,M_p] = perfFCN([child_2(1); child_2(2); child_2(3)]);
   child_2(4) = 1/ISE + 1/t_r + 1/t_s + 1/M_p;
   
end