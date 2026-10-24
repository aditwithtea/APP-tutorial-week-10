from functools import reduce

salaries = [32000, 45000, 38000, 52000, 25000]

# b) Identify employees eligible for the increment.
eligible_salaries = list(filter(lambda salary: salary < 40000, salaries))

# a) Revise salaries: increase salaries below ₹40,000 by 10%.
revised_salaries = list(map(
    lambda salary: salary * 1.10 if salary < 40000 else salary,
    salaries
))

# c) Calculate the total salary expenditure after revision.
total_expenditure = reduce(lambda total, salary: total + salary,
                           revised_salaries, 0)

print("Original salaries:", salaries)
print("Eligible salaries:", eligible_salaries)
print("Revised salaries:", [round(salary, 2) for salary in revised_salaries])
print("Total salary expenditure after revision: ₹", round(total_expenditure, 2))

# d) Functional programming applies clear operations to salary records,
# making filtering and transformation concise and easy to test.
