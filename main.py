
float_num = 5.4

str_var = "SATT"

int_num2, float_num2, str_var2 = 10, 5.4, "SATT"

print(int_num2)

#Assign same value different variable in python
x=y=z = "Bangladesh"
# Check the variable type class

print(x, "is of type",type(x))

num = 1+2j
print(num, "is complex number?", isinstance(1+2j,complex))

a = 1234567890123456789
print(a)

b = 0.1234567890123456789
print(b)
c = 1+2j
print(c)

# python list example
list_example = [2,"java", 'php', 'Dart', 'Flutter']
print(type(list_example))
print("3rd number of item in the list is",list_example[2])

list_number = [4,5,3,2]
if(list_number[0]==list_number[3]):
    print("Available in the list")