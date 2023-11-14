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
 
