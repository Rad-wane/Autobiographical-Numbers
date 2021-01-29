# Finding Autobiographical numbers with n-digits

Dev. by : Rad-Wane  


## Intro:

A generalization of the self-descriptive numbers, called the autobiographical numbers, allow fewer digits than the base, as long as the digits that are included in the number suffice to completely describe it. **e.g. in base 10, 3211000 has 3 zeros, 2 ones, 1 two, and 1 three**. Note that this depends on being allowed to include as many trailing zeros as suit, without them adding any further information about the other present digits.

Because leading zeros are not written down, every autobiographical number contains at least one zero, so that its first digit is nonzero.

Considering a hypothetical case where the digits are treated in the opposite order: the units is the count of zeros, the 10s the count of ones, and so on, there are no such self-describing numbers. Attempts to construct one result in an explosive requirement to add more and more digits.  
Source : [here](https://en.wikipedia.org/wiki/Self-descriptive_number)

## What's an autobiographical number :

An autobiographical number is a number such that the first digit of it counts how many zeros are there in it, the second digit counts how many ones are there and so on.
**For example, 1210 has 1 zero, 2 ones, 1 two and 0 threes.** 

## The program : 

Given `N` (user input) as the number of digits, the task is to find all the Autobiographical Numbers whose length is equal to `N`, and all the Autobiographical Numbers with digits fewer than `N`, in a separate list. 

## Example : 

User inputs 8 : 
```
Enter a number of digits :

8
```

Then, after calculations, the output will be :
```
The list with all autobiographical numbers with 8 digits is :
[42101000]

The list with all autobiographical numbers with at most 8 digits is :
[1210, 2020, 21200, 3211000, 42101000]
```

## Coding :

The program begin by asking for the user input, and finding the max and min values with the given digits : 
```python
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
```
Then, it uses a boolean function called `is_auto_func()` to find out whether a certain number is autobiographical number : 
```python
def is_auto_func(str_nb):
    list_dig=[]    
    len_nb = len(str_nb)
    
    #extracting digits
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
```
And it does so for each and every number from `0` to the max value with `N` digits. Storing the autobiographical number it founds in a list. The list is then processed to find out the `N` autobiographical numbers (the output is given above) : 
```python
for nb in range(max_nb):
    if is_auto_func(str(nb)):
        list_auto_all.append(nb)
for item in list_auto_all:
    if len(str(item)) == nb_dig:
        list_auto.append(item)

if len(list_auto)>0:
    print('\n')
    print('The list with all autobiographical numbers with '+str(nb_dig)+' digits is :' )    
    print(list_auto)
    print('\n')
    print('The list with all autobiographical numbers with at most '+str(nb_dig)+' digits is :' )    
    print(list_auto_all)
else:
    print('No autobiographical number with '+str(nb_dig)+' digits found !')
    
```