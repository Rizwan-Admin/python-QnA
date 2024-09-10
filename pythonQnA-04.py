# compression
# Qt 1] How can you find all the even numbers in a given list of integers using Python?
# sol using list compression
N = [1,2,3,4,5,6,7,8,9,10]
even_N  = [i for i in N if  i % 2 == 0]
print(even_N)

# solution using loop compression
n1=[1,2,3,4,5,6,7,8,9,10]
even_number=[]
for i in n1:
        if i % 2 == 0:
             even_number.append(i)
print(even_number)


# Qt 2] How can you find all the odd numbers in a given list of integers using Python?
n2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd_n=[]
for i in n2:
    if i % 2 ==1:
        odd_n.append(i)
print(odd_n)

# sol using list compression
n3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd_n = [i for i in n3 if n3 % 2 == 1]
print(odd_n)


