# Hexacube-Bookshop
This is a python based project built mainly using pandas matplotlib and data sets which helps in redefining a traditional bookshop.The purpose of the project is to build an application program to reduce the manual work for managing the books, customer, stock, and payment. This application provides a user-friendly environment that provides even less computer- experienced users with selecting books of their interest in seconds. The users can register with their details and can login with their username and passwords on their repeated visits. Users can go through the available books, order their book of choice and the payment can be done on delivery. The frames are created by using PYTHON and PANDAS provides the table storing the data of the users.

CODE:
import pandas as pd
import matplotlib.pyplot as plt
loop1= True
loop2= False
filename="C:\\Users\\AIRPORT SCHOOL 3\\Desktop\\users.csv"
filename2="C:\\Users\\AIRPORT SCHOOL 3\\Desktop\\availability.csv"
filename3="C:\\Users\\AIRPORT SCHOOL 3\\Desktop\\orders.csv"
print("Welcome to HEXACUBE , an online platform to purchase books authored by Chetan Bhagat ")

while loop1:
print("1- Login")
print("2- Register")
print("3- Exit")
choice= int(input("Enter your choice: "))
if choice== 1:
df=pd.read_csv(filename, index_col='user')
uname= input("Enter your username: ")
passw= input("Enter your password: ")
if uname in df.index and passw in df.loc[uname,'passw']:
while True:
print("1. View Available Books ")
print("2. Place Orders")
print("3. Bar Graph of Most Purchased Books")
print("4. Exit")
choice2 = int(input("Enter Your Choice: "))
if choice2==1:
df2=pd.read_csv(filename2, index_col='itemno')
print(df2.iloc[:,:3])
elif choice2== 2:
df3=pd.read_csv(filename3)
df2=pd.read_csv(filename2,index_col='itemno')
itemno= int(input('Enter Item number of the book: '))
qty= int(input('Enter quantity of the books:'))
stock=df2.stock[itemno]
bal= stock- qty
if stock>bal:
df2.order[itemno]=df2.order[itemno]+1
df2.stock[itemno]=bal
to_append3= [uname,itemno,qty]
df_length3=len(df3)
df3.loc[df_length3]=to_append3
df3=df3.set_index('user')
df3.to_csv(filename3)
df2.to_csv(filename2)
print('Purchase successful! Amount to be paid: ',df2.price[itemno])
else:
print('Insufficient stock')
elif choice2==3:
df3=pd.read_csv(filename3)
df2=pd.read_csv(filename2,index_col='itemno')
plt.xlabel('Books')
plt.ylabel('Number of books sold')
plt.title('Books sold')
plt.bar(df2.index,df2.order,width=0.5)
plt.show()
elif choice2==4:
print('Thank You, Visit Again')
break
else:
print('Invalid choice')


elif choice== 2:
uname= input("Enter your username: ")
passw= input("Enter your password: ")
email= input("Enter your email: ")
df=pd.read_csv(filename)
to_append=[uname,passw,email]
df_length=len(df)
df.loc[df_length]=to_append
df=df.set_index("user")
df.to_csv(filename)
elif choice== 3:
print ("Thank You, Visit Again ")
break
else:
print("invalid choice")

print('Thank You, Visit Again')



THE CSV FILES USED ARE

1.	Availability

itemno	Bookname	price	stock	order
1120	FivePointSomeone	350	5	5
1121	One Night AtCallCentre	350	10	4
1122	The3MistakesOfMyLife	450	14	2
1123	2 States	450	13	3
1124	HalfGirlfriend	500	11	5
1125	OneIndianGirl	550	19	5
1126	TheGirlinRoom105	450	16	4
1127	OneArrangedMurder	550	17	3
1128	400 Days	600	23	3



2.	Users

user	passw	email
mathews	jibukuttan	mjibu@gmail.com
ishamol	nish	ishnish@gmail.com
sandmol	sahar	sanhu@gmail.com
akkumol	haak	akha@gmail.com
srinath	joks	srin@gmail.com
bhavya	miss	bmiss@gmail.com
jack	123	jack2@gmail.com






3.	Orders
user	itemno	qty
mathews	1120	1
sandmol	1120	2
akkumol	1121	2
srinath	1121	1
sandmol	1121	1
ishamol	1122	1
sandmol	1122	1
akkumol	1123	2
mathews	1123	1
mathews	1124	1
sandmol	1124	1
ishamol	1124	1
