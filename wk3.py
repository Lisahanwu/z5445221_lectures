happy = False
if happy is True:
    print("I am happy")
print("This will print regardless of the value of happy")

happy = True
if happy:
    print("I am happy")
else:
    banner = None
    interact(banner)

happy = True
if happy:
    print("I am happy")
happy = 5
if happy:
    print("I am happy")
if 5:
print ('5 is Truthy)'
if 'a':
print ('A non-empty string is Truthy')
if [1, 2, 3]:
print ('Non-empty containers are Truthy')

var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']

var1 = 'a'
var2 = 'a'
print(var1 is var2) # --> True
print(var1 == var2) # --> True
var3 = ['a']
var4 = ['a']
print(var3 is var4) # --> False
print(var3 == var4) # --> True

a = 0
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")

happy = True
if happy is True:
    pass

if x > 0 and y is True:
    # Write code for this case later
    pass
elif x <= 0 and y is True:
    # Write code for this case later
    pass
else:
    # Write code for this case later
    pass
name = input('Who are you')
print('Welcome to the class,', name)

# Prompt the user for their weekly working hours
wk = int(input('What is your weekly working hours: '))

# Check the value of wk and calculate the corresponding payment
if wk <= 35:
    payment = 51.45
else:
    payment = 88.9

# Calculate the total payment
pay_calculator = wk * payment

# Print the calculated payment
print("Your weekly payment is:", payment)
print("Total payment for the week is:", pay_calculator)

numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
for i in numbers:
    if i > i+1,
    return i
else return i+1
print(i)

numbers = [3,9,1,5,7,2,11,0.3,12,3,15]
print(max(numbers))
numbers = [3,9,1,5,7,2,11,0.3,12,3,15]
print(max(numbers))

numbers = [3,9,1,5,7,2,11,0.3,12,3,15]
temp_largetest

def compound_interest(principal, rate, time, n=1):
    return principal * (1 + rate / (n * 100)) ** (n * time)
def compound_interest(principal, rate, time, n=1):
    return principal * (1 + rate / (n * 100)) ** (n * time)
