"""
Structured-English
This program is trying to determine which payment option is better (more money).
First Option pays $100 per day for 10 days. The second option pays $1 the first day, $2 the second day, $4 the third day, and 
continues to double for each day until 10 days. There will be two functions to calculate the pay rate.

function1 will calculate the amount for the first option. Function2 will calculate the amount for the second option. 

function1 will output 100 per days * 10 days. 

function2 will loop 10 times, with each time, doubling the amount and add the amount to the total.

If the amount is equal, we output to the user " Option1 and Option2 are the same"
If option1 is better, we output to the user "Option 1 is better"
If option2 is better, we output to the user "Option 2 is better"

"""

"""
Pseudo-code

# option1 
return 100 * 10

#option2
amount = 1
list1 = []
loop 10 times
  add amount to list1
  amount *= 2
  sum = sum of all items in the loop
return sum
#main
var1 = option1
va2 = option2

if var 1 == var2
    "Option 1 and Option 2 pays the same."
if var1 < var2
    "Option 2 is better."
else 
    "Option 1 is better."

main
"""

def option1():
    var1 = 100 * 10
    return var1

def option2():
    amount = 1
    list1 = []
    for i in range(0,10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total





def main():
    answer = ""
    var1 = option1() #1000
    var2 = option2() # 1023
    if var1 == var2:
        answer = "Option 1 and Option 2 pay the same."
    if var1 < var2:
        answer = "Option 2 is better."
    else:
        answer = "option 1 is better"
    print(answer)



main()



