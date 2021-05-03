function [f,X] = DE()
% f - optimal fitness
% X - optimal solution
% CONTROL PARAMETERS %
D = 10;         % dimension of problem
NP = 60;        % size of population       60
F = 0.9        % differentiation constant 0.9
CR = 0.5;       % crossover constant
GEN = 5000;    % number of generations 10000
% Rosebrocks Function
L = -2.048;     % low boundary constraint
H = 2.048;      % high boundary constraint
% Sphere Function
% L = -5.12;     % low boundary constraint
% H = 5.12;      % high boundary constraint

% *************************** %
% ** ALGORITHM’S VARIABLES ** %
% *************************** %
X = zeros(D,1);     % trial vector
Pop = zeros(D,NP);  % population
Fit = zeros(1,NP);  % fitness of the population
iBest = 1;          % index of the best solution
r = zeros(3,1);     % randomly selected indices

% *********************** %
% ** CREATE POPULATION ** %
% *********************** %
% initialize random number generator
rand('state',sum(100*clock));
for j = 1:NP                        % initialize each individual
    Pop(:,j) = L + (H-L)*rand(D,1); % within b.constraints
    Fit(1,j) = fnc(Pop(:,j));       % and evaluate fitness
end
% ****************** %
% ** OPTIMIZATION ** %
% ****************** %
for g = 1:GEN           % for each generation
    for j = 1:NP        % for each individual
        % choose three random individuals from population,
        % mutually different and different from j
        r(1) = floor(rand()* NP) + 1;
        while r(1)==j
            r(1) = floor(rand()* NP) + 1;
        end
        r(2) = floor(rand()* NP) + 1;
        while (r(2)==r(1))||(r(2)==j)
            r(2) = floor(rand()* NP) + 1;
        end
        r(3) = floor(rand()* NP) + 1;
        while (r(3)==r(2))||(r(3)==r(1))||(r(3)==j)
            r(3) = floor(rand()* NP) + 1;
        end
        % create trial individual
        % in which at least one parameter is changed
        Rnd = floor(rand()*D) + 1;
        for i = 1:D
            if ( rand()<CR ) || ( Rnd==i )
                X(i) = Pop(i,r(3)) + F * (Pop(i,r(1)) - Pop(i,r(2)));
            else
                X(i) = Pop(i,j);
            end
        end
        % verify boundary constraints
        for i = 1:D
            if (X(i)<L)||(X(i)>H)
                X(i) = L + (H-L)*rand();
            end
        end
        % select the best individual
        % between trial and current ones
        % calculate fitness of trial individual
        f = fnc(X);
        % if trial is better or equal than current
        if f <= Fit(j)
            Pop(:,j) = X;
             % replace current by trial
            Fit(j) = f ;
            % if trial is better than the best
            if f <= Fit(iBest)
            iBest = j ;
             % update the best’s index
            end
        end
    end
end
% ************* %
% ** RESULTS ** %
% ************* %
f = Fit(iBest);
X = Pop(:,iBest);
end

% ============================================== %
function f = fnc(X)
    % fitness function
    n = length(X);
    f = 0;
    % Rosenbrock's function
    for i = 1:n-1
        f = f + 100 * ( X(i,1)*X(i,1) - X(i+1,1))^2 + (1 - X(i,1))^2;
    end
    % Sphere function
%     for i = 1:n
%         f = f +  X(i,1)^2 ;
%     end
end


