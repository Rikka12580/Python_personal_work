from random import randint

#first die rolls
num_array1 = []
for x in range (0, 4):
    num_array1.append(randint(1,6))
    #print(num_array1)
    x += 1
num_array1.sort()
print(num_array1)
added1 = num_array1[1]+num_array1[2]+num_array1[3]
print(added1)

#second die rolls
num_array2 = []
for x in range (0, 4):
    num_array2.append(randint(1,6))
    #print(num_array2)
    x += 1
num_array2.sort()
print(num_array2)
added2 = num_array2[1]+num_array2[2]+num_array2[3]
print(added2)

#third die rolls
num_array3 = []
for x in range (0, 4):
    num_array3.append(randint(1,6))
    #print(num_array3)
    x += 1
num_array3.sort()
print(num_array3)
added3 = num_array3[1]+num_array3[2]+num_array3[3]
print(added3)

#forth die rolls
num_array4 = []
for x in range (0, 4):
    num_array4.append(randint(1,6))
    #print(num_array4)
    x += 1
num_array4.sort()
print(num_array4)
added4 = num_array4[1]+num_array4[2]+num_array4[3]
print(added4)
all_rolls = [added1, added2, added3, added4]
print(all_rolls)
all_rolls.sort()
print(all_rolls)
print(max(all_rolls))
if max(all_rolls) == all_rolls[0]:
    print('your best rolls were ((', num_array1[3], num_array1[2], num_array1[1], ')) from your first set of rolls.')
elif max(all_rolls) == all_rolls[1]:
    print('your best rolls were ((', num_array2[3], num_array2[2], num_array2[1], ')) from your second set of rolls.')
elif max(all_rolls) == all_rolls[2]:
    print('your best rolls were ((', num_array3[3], num_array3[2], num_array3[1], ')) from your third set of rolls.')
elif max(all_rolls) == all_rolls[3]:
    print('your best rolls were ((', num_array4[3], num_array4[2], num_array4[1], ')) from your forth set of rolls.')