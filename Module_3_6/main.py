salary = [43986,54730, 98476, 36584, 95749]
print(round(sum(salary), 1) / len(salary))
print(round(max(salary), 1), 'MAxinum Salary')
print(round(min(salary), 1), 'Minimum Salary')
staff = ('A', 'B', 'C', 'D')
zipped = zip(staff, salary)
print(list(zipped))
print(dict(zipped))
print(help(zipped['D']))
