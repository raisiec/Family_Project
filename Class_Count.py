# Author: Raisie & Daddy
# Date: 11/3/2022
# Name: Class Splitter

a_file = open('data.txt')
a_content = a_file.read()
family = a_content.splitlines()

A = []
B = []
C = []
D = []
E = []

for i in range(len(family)):
  entry = family[i].split()
  #print(entry[0])
  if (entry[0] == 'G2A'):
    A.append(family[i])
  if (entry[0] == 'G2B'):
    B.append(family[i])
  if (entry[0] == 'G2C'):
    C.append(family[i])
  if (entry[0] == 'G2D'):
    D.append(family[i])
  if (entry[0] == 'G2E'):
    E.append(family[i])

def printList(name, input):
  print('Class G2' + name + ': ' + 'No. of families: ' + str(len(input)))
  for i in range(len(input)):
    print(input[i])
  print('')

printList('A', A)
printList('B', B)
printList('C', C)
printList('D', D)
printList('E', E)
