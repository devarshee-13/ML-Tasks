# -*- coding: utf-8 -*-
"""task1_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uCPX8Cm6fXS8eZ03b-mObr1hJA-wXm92
"""

creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot',
'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot',
'green_light','red_light', 'red_light', 'green_light', 'you_got_shot','red_light', 'you_got_shot']

next_game=[]
x='green_light'
for i in creepy_doll:
  if i==x:
    next_game.append(i)
print(next_game)
print(next_game.count('green_light'))