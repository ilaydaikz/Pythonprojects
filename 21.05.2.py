# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:24:54 2022

@author: ilayd
"""

#DÖNGÜLER
#range(baslangıc degeri, bitis degeri, degisim miktarı)
range(5)
#for item in loop print(item)
for item in range(5):
    print(item)
for i in range(7, 16):
   if i>= 12:
     print("break")
     break
   else:
      print(i)
     
        
count = 1
while count < 6:
    print(count)
    count += 1
#İC İCE KULLANILAN DÖNGÜLER
rows = 5
for i in range(1, rows + 1):
  for j in range(1, i+1):
    print("*", end= " ")
  print()
  #yanyana yazamyi saglar
for item in range(5):
    print(str(item), end=" ")
    
   
      