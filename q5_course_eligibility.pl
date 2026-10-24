% Facts: student(Name, PythonResult, DataStructuresResult).
student(arun, pass, pass).
student(bala, pass, fail).
student(charan, pass, pass).
student(divya, fail, pass).

% Rule: a student is eligible only if both subjects are passed.
eligible(Name) :-
    student(Name, pass, pass).

% Query: ?- eligible(Name).
% Expected answers: Name = arun ; Name = charan.
