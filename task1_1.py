# -*- coding: utf-8 -*-
"""task1_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18SRLQC7wf9SbGFX-EMUexQQgTcCUIs7I
"""

modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr','StELLa']

indices=[]
characters=[]
for i,j in enumerate(modern_family):
  indices.append(i)
  characters.append(j)

print(indices)

print(characters)

lowercase=[]
replaced=[]
for i in characters:
  lowercase.append(i.lower())
print(lowercase)
for i in lowercase:
  replaced.append(i.replace('_','-'))
print(replaced)

length = lambda seq:len(seq)
temp=[]
temp = list(map(length, characters))
print(temp)

indices = list(map(sum,zip(indices,temp)))
print(indices)

indices.sort(reverse=True)
print(indices)

Phew_finally = {}
for key in indices:
    for value in characters:
        Phew_finally[key] = value
        characters.remove(value)
        break
print(Phew_finally)