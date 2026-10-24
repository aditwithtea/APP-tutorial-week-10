% Facts: employee(Name, ExperienceYears, TrainingStatus, Rating).
employee(ravi, 6, completed, 5).
employee(priya, 3, completed, 4).
employee(kumar, 8, not_completed, 5).
employee(meena, 7, completed, 4).

% Rule: at least 5 years' experience, completed training, rating >= 4.
promotion_eligible(Name) :-
    employee(Name, Years, completed, Rating),
    Years >= 5,
    Rating >= 4.

% Query: ?- promotion_eligible(Name).
% Expected answers: Name = ravi ; Name = meena.
