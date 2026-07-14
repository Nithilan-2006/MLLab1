#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = input()
l = list(a)
count = len(l)
vcount = 0
for i in l:
    if i in "aeiou":
        vcount = vcount+1
ccount = count-vcount
print("Number of vowels : ",vcount)
print("Number of consonants : ",ccount)


# In[10]:


r = int(input("Enter the number of rows : "))
A = []
B = []
print("Enter the elements of matrix A : ")
for i in range(r):
    row = list(map(int,input().split()))
    A.append(row)

print("Enter the elements of matrix B : ")
for j in range(r):
    row = list(map(int,input().split()))
    B.append(row)

print(A)
print(B)

C = [[0 for _ in range(r)] for _ in range(r)]

for i in range(r):
    for j in range(r):
        for k in range(r):
            C[i][j] += A[i][k] * B[k][j]

print("\nResultant Matrix C (A x B):")
for row in C:
    print(row)


# In[12]:


lst1 = [1,2,4,5]
lst2 = [2,3,5]
c = []
for i in lst1:
    for j in lst2:
        if i == j:
            c.append(i)

for a in c:
    print(a)


# In[13]:


r = int(input("Enter the number of rows : "))
A = []
print("Enter the elements of matrix A : ")
for i in range(r):
    row = list(map(int,input().split()))
    A.append(row)

c = len(A[0])
T = [[0 for _ in range(r)] for _ in range(c)]

for i in range(r):
    for j in range(c):
        T[j][i] = A[i][j]

print("\nTranspose Matrix T:")
for row in T:
    print(row)


# In[14]:


import random

numbers = [random.randint(100, 150) for _ in range(100)]

mean = sum(numbers) / len(numbers)

sorted_nums = sorted(numbers)
median = (sorted_nums[49] + sorted_nums[50]) / 2

frequencies = {}
for num in numbers:
    frequencies[num] = frequencies.get(num, 0) + 1

mode = max(frequencies, key=frequencies.get)

print("Generated Numbers:", numbers)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode} (appears {frequencies[mode]} times)")


# In[ ]:




