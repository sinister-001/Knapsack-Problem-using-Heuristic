# Knapsack-Problem-using-Heuristic

#### In this repository we are going to see how to solve Knapsack Problem using Heuristic Approach.
#### Here I have used Simulated Annealing as my Heurisitc Approach to solve this *Binary Knapsack*. We will go through the Simulated Annealing detailed in this repository.
## Simulated Annealing
#### The algorithm is inspired by annealing in metallurgy where metal is heated to a high temperature quickly, then cooled slowly, which increases its strength and makes it easier to work with.

#### The annealing process works by first exciting the atoms in the material at a high temperature, allowing the atoms to move around a lot, then decreasing their excitement slowly, allowing the atoms to fall into a new, more stable configuration.
#### The simulated annealing optimization algorithm can be thought of as a modified version of stochastic hill climbing.

#### Stochastic hill climbing maintains a single candidate solution and takes steps of a random but constrained size from the candidate in the search space. If the new point is better than the current point, then the current point is replaced with the new point. This process continues for a fixed number of iterations.

#### Simulated annealing executes the search in the same way. The main difference is that new points that are not as good as the current point (worse points) are accepted sometimes.

#### A worse point is accepted probabilistically where the likelihood of accepting a solution worse than the current solution is a function of the temperature of the search and how much worse the solution is than the current solution.

#### The initial temperature for the search is provided as a hyperparameter and decreases with the progress of the search. A number of different schemes (annealing schedules) may be used to decrease the temperature during the search from the initial value to a very low value, although it is common to calculate temperature as a function of the iteration number.

#### A popular example for calculating temperature is the so-called “fast simulated annealing,” calculated as follows
#### temperature = initial_temperature / (iteration_number + 1)
#### We add one to the iteration number in the case that iteration numbers start at zero, to avoid a divide by zero error.

#### The acceptance of worse solutions uses the temperature as well as the difference between the objective function evaluation of the worse solution and the current solution. A value is calculated between 0 and 1 using this information, indicating the likelihood of accepting the worse solution. This distribution is then sampled using a random number, which, if less than the value, means the worse solution is accepted.

#### This is called the metropolis acceptance criterion and for minimization is calculated as follows:

#### criterion = exp( -(objective(new) – objective(current)) / temperature)
#### Where exp() is e (the mathematical constant) raised to a power of the provided argument, and objective(new), and objective(current) are the objective function evaluation of the new (worse) and current candidate solutions.

#### The effect is that poor solutions have more chances of being accepted early in the search and less likely of being accepted later in the search. The intent is that the high temperature at the beginning of the search will help the search locate the basin for the global optima and the low temperature later in the search will help the algorithm hone in on the global optima.
