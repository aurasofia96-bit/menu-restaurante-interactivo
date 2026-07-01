menu=['🍔 Cheeseburger','🍟 Fries', '🥤 Soda','🍦 Ice Cream','🍪 Cookie','🍕 Pizza']
num=len(menu)
def get_item(x):
  orden=menu[x-1]
  return orden
def welcome():
  print('Bienvenidos a cookie Love.')
  print('Manú:')
  for i in range (0,num):
    print(i+1, menu[i])
welcome()
seleccion=int(input('¿Que vas a ordenar?'))
while seleccion<1 or seleccion>num:
  print(f'Error: Valor no valido escoja un número del 1 al {num}')
  seleccion=int(input('¿Que vas a ordenar?'))
orden=get_item(seleccion)
print(f'Ordenaste {orden}')