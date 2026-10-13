#1
name = "jayapriya"
print(name)

#age,height,student datype nokan
age = 20
height = 135
student = True
print(type(age))
print(type(height))
print(type(student))

#three variables print cheyan
name = "jayapriya"
age = 20
place = "thrissur"
print(name,age,place)

#swap
a = 30
b = 10
a,b = b,a
print(a)
print(b)

#first name last name combine cheyan
first_name = "jaya"
last_name = "priya"
full_name = first_name+last_name
print(full_name)


#value 100 il ninn 200 akka
number = 100
number = 200
print(number)

#type conversion
#25ne float akkan
a = float(25)
print(a)

#float 19.99 ne integar akka
a = int(19.99)
print(a)

#string 500 ne integar akki athil 100 add akkan
a = int("500")
print(a+100)

#take two numbers as input and print their sum
a=int(input("first number"))
b=int(input("second number"))
print(a+b)
#take a decimal number as input and convert it into float
a=float(input("enter a number"))
print(float(a))

#output int 8.9 kittnnam
print(int(8.9))

#output of float(10)
print(float(10))

#output of str(25)+str(15)
print(str(25)+str(15))

#output of bool values
print(bool(2))
print(bool(1))
print(bool(""))

#what happens when you execute int("hello")?
print(int("hello"))

#3.arthemetic
#find the output

a=15
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#area of a rectangle
length=10
width=5
area = length * width
print(area)


#total price of three products
a=200
b=300
c=400
total=a+b+c
print(total)

#calculate square and cube
num = int(input("Enter the number"))
print(num**2)
print(num**3)

#convert minutes into seconds
minute = int(input("enter minutes"))
seconds = minute *60
print(seconds)
#calculate total and average marks
a=75
b=80
c=90
total=a+b+c
average=total/3
print(total)
print(average)

# calculate total cost
price = int(input("Enter the price:"))
quantity = int(input("Enter the quantity: "))
total = price * quantity
print(total)

#4.comparison and logical operator
#predict the output
print(10>5)
print(10==10)
print(7!=7)
print(15<=20)

#27
print(10>5 and 8<12)
print(10<5 or 8<12)
print(not True)

# difference between and or
print(5>2 and 10>5)
print(5<2 or 10>5)

#29
a=10
b=20
print(a>b)
print(a<b)
print(a==b)

#30
#a.
print(25>15)

#b.
print(10==10)

#c.
print(8!=5)

#d.
print(20>10 and 15<20)

#31.
x=10

x+=5
print(x)

x*=2
print(x)

x-=4
print(x)

#difference between x = x + 5 and x += 5  
#1.
x=10
x=x+5
print(x)

#2.
x=10
x += 5
print(x)

#33.
x=17
print(x//5)
print(x%5)

#caluculate final price after 10% discout
price = 1000
disount = price*10/100
final_price = price = disount
print(final_price)


#35.
a=5
b=2
print(a**b+b*3)
print((a+b)*3)