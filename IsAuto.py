# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:04:23 2021

@author: radwa
"""

list_auto = []
#if str_nb =='a':
 #   sys.exit()
print('Enter a number of digits :')
nb_dig=int(input())
max_nb=''
min_nb='1'

for u in range(nb_dig):
    max_nb += '9'
for u in range(nb_dig-1):  
    min_nb += '0'
    
max_nb=int(max_nb)
min_nb=int(min_nb)


def is_auto_func(str_nb):
    list_dig=[]    
    len_nb = len(str_nb)
    
    #extacting digits
    for i in range(len_nb):
        list_dig.append(int(str_nb[i]))    
 
    #verifying auto    
    for i in range(len_nb):
        if list_dig.count(i) == list_dig[i]:
            is_auto = True
        else:
            is_auto = False
            break
    
    if is_auto :
        return True
    else:
        return False
        

for nb in range(min_nb,max_nb,1):
    if is_auto_func(str(nb)):
        list_auto.append(nb)

if len(list_auto_all)>0:
    print('\n')
    print('The list with all autobiographical numbers with '+str(nb_dig)+' digits is :' )    
    print(list_auto)
else:
    print('No autobiographical number with '+str(nb_dig)+' digits found !')
    
    

    
        
        
    