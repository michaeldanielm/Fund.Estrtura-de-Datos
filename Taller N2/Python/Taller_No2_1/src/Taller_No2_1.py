# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.




array =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100


]


n = len(array)
minimo = abs(array[0] - array[1])

for i in range (n):
  
  for j in range (n):
    
    if i!=j:
      
      minimo = abs(array[i]-array[j]) if abs(array[i] - array[j]) < minimo else minimo
 

print ("Numeros del Array ")
print (array )
print("El Minimo Numero Del Array es ")
# ingrese el mayor numero primero y luego el menor numero
array = input(80-5)
print (minimo)
