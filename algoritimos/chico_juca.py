alturaChico = 1.50
alturaZe = 1.10
anos = 0

while alturaChico >= alturaZe:
    anos += 1
    alturaChico += 0.02
    alturaZe += 0.03

print('Foi necessário {} anos para Zé ficar maior que chico'.format(anos))