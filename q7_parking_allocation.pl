% Facts: parking_slot(Slot, VehicleType, Availability).
parking_slot(s1, car, available).
parking_slot(s2, bike, occupied).
parking_slot(s3, car, available).
parking_slot(s4, bike, available).
parking_slot(s5, car, occupied).

% Rule: a slot is available for a particular vehicle type.
available_slot(Slot, VehicleType) :-
    parking_slot(Slot, VehicleType, available).

% Query for available car slots: ?- available_slot(Slot, car).
% Expected answers: Slot = s1 ; Slot = s3.
