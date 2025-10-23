import random

attempts = 0
low, high = 0, 100

dollars = random.randint(low, high)

print(f"\n####  Oscar has ${dollars} in the Bank ###")
print("++++++++++++++++++++++++++++++++++++++++++++++\n")

while True:
    attempts += 1
    print(f"Suggestion:{(low + high) // 2}") 
    response = int(input(f"Attempt number:{attempts}: "))
    
    if response == dollars:
         print(f"\nYou guessed ${dollars} in only {attempts} tries!\n")
         break
    
    if response < dollars:
         print(f"Your guess of {response} was too low\n")
         low = response
         continue
    
    else:
        print(f"Your guess of {response} was too high\n")
        high = response
        continue
    
    break
