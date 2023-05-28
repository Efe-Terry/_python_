print('SALARY - TAX CALCULATOR')
print('Tax conversion in %')

salary = input('Enter Salary: ')
tax_on_salary = input('Enter Tax %: ')

print('********************')

tax = int(salary)*(int(tax_on_salary)/100)

print(f'Tax is {tax_on_salary}% of your Salary {salary}: ', int(salary) - tax)

print('********************')

print('Main Salary: ', salary)
print('Salary after Tax: ', int(salary) - tax)

##Tax formula = salary*(percent/100)##
print('SALARY - TAX CALCULATOR')