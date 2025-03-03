my_list=[1, 3, 4, 10.2, True, "Hello", "Hi"]

#accessing elements
print(my_list[2])  #it will accessing element at index 2  output: 4
print(my_list[-1])  #last element o/p: Hi

#modifying list

my_list.append(30)  #add the element at the end 
print(my_list)

my_list[2]=24      #adds the element at the index 2
print(my_list)


#Removing the elements
my_list.remove(24)
print(my_list)

my_list.pop(2)  #removes element at the index 2
print(my_list)