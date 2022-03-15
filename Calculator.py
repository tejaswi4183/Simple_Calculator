
z=1
def Addition(a,b):
	return a+b
def Substraction(a,b):
	return a-b
def Multiplication(a,b):
	return a*b
def Division(a,b):
	return a//b
def ModuloDivision(a,b):
	return a%b

while(z):
	a=int(input("Enter First Number:"))
	b=int(input("Enter Second Number:"))
	print("Menu:\n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Modulo Division \n")
	choice=int(input("Enter One Option to perform Operation:"))
	if(choice==1):
		result=Addition(a,b)
		print(a,"+",b,"=",result)
	elif(choice==2):
		result=Substraction(a,b)
		print(a,"-",b,"=",result)
	elif(choice==3):
		result=Multiplication(a,b)
		print(a,"*",b,"=",result)
	elif(choice==4):
		result=Division(a,b)
		print(a,"/",b,"=",result)
	elif(choice==5):
		result=ModuloDivision(a,b)
		print(a,"%",b,"=",result)
	else:
		print("Please Select Correct Choice\n")
	z=int(input("enter 0 to stop the loop:"))
	
	
	
	
