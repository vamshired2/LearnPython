str ="Hello world"

#inbuilt functions
print(str.upper())  #converts to uppercase
print(str.lower())   #converts to lower case
print(str.title())   #Converts first letter of each word to uppercase
print(str.swapcase()) #Swaps case of all letters

print(str.startswith("He"))
print(str.endswith("ld"))
print(str.index('w'))

str1=" Hello "
print(str1.lstrip())
print(str1.rstrip())

#split( real time scenario)
arn="arn:aws:iam::123456789012:user/johndoe"
print(arn.split(":") [5])