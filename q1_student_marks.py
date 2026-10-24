from functools import reduce

students = [
    ("Arun", 78),
    ("Bala", 45),
    ("Charan", 92),
    ("Divya", 50),
    ("Esha", 36)
]

# a) Identify students who scored 50 marks or above.
qualified = list(filter(lambda student: student[1] >= 50, students))

# b) Award 5 grace marks, without allowing a score above 100.
grace_marks = list(map(
    lambda student: (student[0], min(student[1] + 5, 100)),
    students
))

# c) Calculate the total marks after grace marks.
total_marks = reduce(lambda total, student: total + student[1], grace_marks, 0)

print("Students scoring 50 or above:", qualified)
print("Marks after grace marks:", grace_marks)
print("Total marks after grace marks:", total_marks)

# d) Lambda functions are short anonymous functions, useful here for
# expressing simple conditions and transformations directly.
