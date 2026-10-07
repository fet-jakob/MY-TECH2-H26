import numpy as np

def tax(income):
    """Retrun taxes owed for a given income

    Parameters
    -------
    income
        gross income

    Returns

    -----
    Tax owed
    """

    #Write your implementation here

    if income < 300000:
        taxes = 0
    elif 300000 <= income <= 700000:
        taxes = (income-300000) * 0.20
    else:
        taxes = (700000-300000) * 0.2 + (income - 700000) * 0.35

    return(taxes) 

incomes = np.linspace(0,1200000,13)
taxes_loop = np.zeros(13)
after_tax = np.empty(13)

for i in range(len(incomes)):
    taxes_loop[i] = tax(incomes[i])
for i in range(len(incomes)):   
    after_tax[i] = incomes[i] - taxes_loop[i]
   
#print(incomes)
#print(taxes_loop)
#print(after_tax)

#print(f'Gross income: {incomes:10.0f}; '
#      f'Taxes: {taxes_loop:10.0f}; '
#      f'Net income {after_tax:10.0f}')


print(f'{"Gross income":>14} {"Taxes":>12} {"Net income":>12}')
for gross, tax_owed, net in zip(incomes, taxes_loop, after_tax):
    print(f'{gross:>14,.0f} {tax_owed:>12,.0f} {net:>12,.0f}')



