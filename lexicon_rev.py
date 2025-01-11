'''s = 'Python'
print((s[4], s[:4], s[1:4], s[::-1]))

l = [3,7,[1,4,'hello']]
l[2][2]='goodbye'
print(l)


d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3= {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'],d2['k1']['k2'],d3['k1'][0]['nest_key'][1] [0])

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

age = 4        
name = "Sammy"
 
print(f"Hello my dog's name is {name} and he is {age} years old")

base,expo=map(int, input('enter the base and exponent with spaces >> ').split())
print(base,expo)
result=1
for _ in range(expo):
  result*=base
print(result)

my_tuple=(2,3,4,5,14,5)
print(sum(my_tuple))
my_tuple=(2,3,4,5,14,5)
sum=0
for i in my_tuple:
  sum+=i
print(sum)

my_tuple=(2,3,4,5,14,5)
even=[num for num in my_tuple if num%2==0]
print(tuple(even))

dict1={
  'key1':'value1',
  'key2':'value2'
}
dict2={
  'keyss1':'valuess1',
  'key2':'valuess2'
}

murge_dict={**dict1,**dict2}
print(murge_dict)

user_list=[]
while(True): 
 user_input=input('enter the number after words type exit >> ')
 if(user_input=='exit'):
  break
 else:
  user_list.append(int(user_input))
print(user_list)
print('Even number n the list is ::')
user_even=[num for num in user_list if num%2==0]
print(user_even)

user_string=input('enter your name >> ')
print(user_string[::-1])

# Using a lambda function to square a number
 
square=lambda x:x**2
print(square(5))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=list(filter(lambda x:x%2==0, numbers))
print(even)


prices = [100, 200, 300, 400, 500]
disc_price=list(map(lambda x:x*0.9 , prices))
print(disc_price)


numbers = [-5, -2, 0, 1, 3, 7]
positive=list(filter(lambda x:x>0, numbers))
print(positive)
pos_squ=list(map(lambda x:x**2, positive))
print(pos_squ)

def arrayCheck(num):
  return '123' in ''.join(map(str,num))
     


 

print(arrayCheck([1, 1, 2, 3, 1])  )
  
print(arrayCheck([1, 1, 2, 4, 1])  )
print(arrayCheck([1, 1, 2, 1, 2, 3])  )


def stringBits(str):
  print(str[::2])

stringBits('Hello')  
stringBits('Hi')  
stringBits('Heeololeo')

def doubleChar(str):
  result=''
  for i in str:
    result+=(i*2)
  return result

print(doubleChar('The')  )
print(doubleChar('AAbb'))  
print(doubleChar('Hi-There'))  ''' 


def count_evens(num):
   
  even=[i for i in num if i%2==0]
  return (len(even))
print(count_evens([2, 1, 2, 3, 4]) )
print(count_evens([2, 2, 0])  )
print(count_evens([1, 3, 5])  )



  



