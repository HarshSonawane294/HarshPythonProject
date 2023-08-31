import mysql.connector as msqlc
from tkinter import*
from tkinter import messagebox
con=msqlc.connect(host='localhost',user='root',password='',database='Harsh')
print("opened sucess")
c=con.cursor()
def create():
	q1=("CREATE TABLE IF NOT EXISTS Employee(EID int,Ename varchar(50),address varchar(30),Salary bigint)")
	try:
		c.execute(q1)
		messagebox.showinfo(title="Info",message="Employee(EID int,Ename varchar(50),\naddress varchar(30),Salary int)\nis created!")
	except:
		pass
	con.commit()
	
tk=Tk()
tk.geometry('400x400+50+50')
tk.resizable(True, True)

name=StringVar()
name.set("Ename goes here")
Salary=IntVar()
Salary.set("Salary  goes here")
address=StringVar()
address.set("address goes here")
id=IntVar()
query=StringVar()
query.set('optional query')
agree = StringVar()    #_____->is used in RB_changed function
query.set('optional query')
Hvalue= StringVar()
Hvalue.set('value goes here')


def RB_changed():
                        query.set(f"delete from Employee  where {agree.get()}={Hvalue.get()}")
                        try:
                        	q=query.get()
                        	c.execute(q)
                        	query.set('')
                        	messagebox.showinfo(title="success", message=f'"{q} is performed successfully"')
                        except Exception as e:
                        		messagebox.showerror(title="info", message=f'"{e}"')
                        		messagebox.showinfo(title='Note',message=f"\nnow first Enter value belongs to {agree.get()} "+f'\n then select field:{agree.get()}')
                        
                        

def warning():
		   messagebox.showwarning("Warning",
     "primary key cannot be null")

def InsertAll():
	n,s=(0,'')
	n,s,s1,s2=id.get(),f'{name.get()}',f'{address.get()}',Salary.get()
	if name.get()=='':
		s="none"
		s1='none'
	q=f'insert into Employee(EID,Ename,address,Salary) values({n},"{s}","{s1}",{s2})'
	try:	
		c.execute(q)
	except Exception as e:
		messagebox.showerror("Error", f'"{e}"')
	c.commit()
		

def select():
	str='\n'
	q="select * from Employee"
	try:
		c.execute(q)
		for i in c:
			str=str+f"{i}\n"
	except Exception as e:
		messagebox.showerror("Error", f'"{e}"')
	text.insert(INSERT, str)
	text.tag_add(str, "2.0", "50.0")
	text.tag_config(str, background="light blue", foreground="brown",font=("Times New Roman",9,"italic bold"))
	
   	
def error():
    messagebox.showerror("Error", "Error in delete operation")
    
def Info():
    messagebox.showerror(title="Info",message="Modify delete query first")


def delete():
	if query.get()=='' or query.get()== 'optional query':
								Info()
								query.set("delete from Employee  where referencefield='value'")
	else:
										try:
											q=query.get()
											c.execute(q)
											query.set('')
											messagebox.showinfo(title="success", message=f'"{q} is performed successfully"')
										except Exception as e:
											messagebox.showerror(title="info", message=f'"{e}"')
											Info()
													

def info():
    messagebox.showerror(title="Info",message="Modify update query first")

def update():
							if query.get()=='' or query.get()== 'optional query':
								query.set("update Employee set fieldName='value' where condition")
							else:
									try:
										q=query.get()
										c.execute(q)
										messagebox.showinfo(title="success", message=f'"{q} is performed successfully"')
										q.set("")
										c.commit()
									except Exception as e:
										messagebox.showerror(title="info", message=f'"{e}"')
										info()
				
	
def drop():
		try:
			q="drop table Employee"
			c.execute(q)
		except Exception as e:
			messagebox.showerror(title="info", message=f'"{e}"')

def query_ok():
			str='\n'
			q=query.get()
			try:
				c.execute(q)
				cur=c.execute(q)
				for i in cur:
					str=str+f"{i}\n"
				text.insert(INSERT, str)
				text.tag_add(str, "2.0", "50.0")
				text.tag_config(str, background="light blue", foreground="brown",font=("Times New Roman",8,"italic"))
				messagebox.showinfo(title="success", message=f'"{q} is performed successfully"')
			except Exception as e:
				messagebox.showerror(title="Error", message=f'"{e}"')
	
scrollbar = Scrollbar(tk,bg='gold')
text = Text(tk,width=52,height=300,bg='gold',yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview,bd=5,relief=SUNKEN)
scrollbar.place(x=1700,y=600,relheight=0.35)
p=PanedWindow(tk,orient=VERTICAL,bd=15,width=400,height=600,bg="RED",relief=SUNKEN)
#panel for login
p2=PanedWindow(tk,orient=VERTICAL,bd=5,width=600,height=300,relief=RAISED,bg="white")
 
def TextOP():
	text.pack()
	s="EID     |         Ename       |     address      |   Salary\n"
	text.insert(INSERT, s)
	text.tag_add(s, "1.0", "2.0")
	text.tag_config(s, background="yellow", foreground="blue",font=("Times new Roman",9,"bold"))

e1=Entry(p,bg='gray',font=('arial',8,'italic bold'),bd='8',justify="right",width=10,textvariable=id)
e2=Entry(p,bg='gray',font=('arial',8,'italic bold'),bd='8',justify="right",width=15,textvariable=name)
e4=Entry(p,bg='gray',font=('arial',8,'italic bold'),bd='8',justify="right",width=15,textvariable=Salary)
e3=Entry(p,bg='gray',font=('arial',8,'italic bold'),bd='8',justify="right",width=20,textvariable=address)
e5=Entry(p,bg='dark gray',font=('arial',10,'italic bold'),bd=8,justify="right",width=35,textvariable=query)
e6=Entry(p,bg='dark gray',font=('arial',8,'italic bold'),bd=8,justify="right",width=15,textvariable=Hvalue)
def panel():
	p.pack()	
	w=Label(p,text="Enter EID,EName,address,Salary fields as per query need before performing operation",wraplength=0,fg="red",bg='yellow',font=("arial",8,"bold")).grid(row=0,column=0,columnspan=7)
	e1.grid(column=0,row=2)
	e2.grid(column=1,row=2)
	e3.grid(column=2,row=2)
	e4.grid(column=3,row=2)
	e5.grid(column=0,row=1,columnspan=5)
	w2=Label(p,text="Type Query here:->",fg="red",wraplength=300,bg='yellow',font=("arial",8,"bold")).grid(row=1,column=0)
	
	b=Button(p,text="selectAllData",font=("arial",8,"bold"),command=select,bg="yellow",activebackground="green",activeforeground="white",bd=8,relief=RAISED).grid(row=3,column=2)
	b2=Button(p,text="InsertFieldData",font=("arial",8,"bold"),command=InsertAll,bg="yellow",activebackground="green",activeforeground="white",bd=8,relief=RAISED).grid(row=2,column=4)
	b5=Button(p,text="Create table",font=("arial",8,"bold"),command=create,bg="yellow",width=6,activebackground="green",activeforeground="white",bd=8,relief=RAISED).grid(row=3,column=0)
	b4=Button(p,text="Drop table",font=("arial",8,"bold"),command=drop,bg="yellow",activebackground="green",activeforeground="white",bd=8,relief=RAISED).grid(row=3,column=1)
	b3=Button(p,text="DeleteRowData",font=("arial",8,"bold"),command=delete,bg="yellow",activebackground="green",activeforeground="white",bd=8,relief=RAISED).grid(row=3,column=3)
	b7=Button(p,text="Update",font=("arial",8,"bold"),command=update,bg="yellow",activebackground="green",activeforeground="white",bd=8,relief=RAISED).grid(row=3,column=4)
	b6=Button(p,text="Click to perform",font=("arial",8,"bold"),command=query_ok,bg="light blue",fg="red",activebackground="green",width=10,activeforeground="white",bd=5,relief=RAISED).grid(row=1,column=4)
	w3=Label(p,text="Delete row Data with fieldName:->",fg="brown",wraplength=760,bg='light green',font=("arial",8,"bold")).grid(row=4,column=0,columnspan=5)
	
	e6.grid(row=5,column=0)
	options={"EID":"EID","Ename":"Ename","address":"address","Salary":"Salary"}
	Radiobutton(p,text="Eid",command=RB_changed,variable=agree,value=options["EID"]).grid(row=5,column=1)
	Radiobutton(p,text="Ename",command=RB_changed,variable=agree,value=options["Ename"]).grid(row=5,column=2)
	Radiobutton(p,text="address",command=RB_changed,variable=agree,value=options["address"]).grid(row=5,column=3)
	Radiobutton(p,text="Salary",command=RB_changed,variable=agree,value=options["Salary"]).grid(row=5,column=4)
	
	               
#.pack(side=LEFT,ipadx=3)


""""##################"""
def Loginform():
    global  message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    p2.pack()
    Label(p2,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    Label(p2, text="").pack()
    Label(p2, text="Enter Username * ").pack()
    Entry(p2, textvariable=username).pack()
    Label(p2, text="Enter password * ").pack()
    Entry(p2, textvariable=password ,show="*").pack()
    Label(p2, text="",textvariable=message).pack()
    Button(p2, text="Login", width=10, height=1, bg="orange",command=login).pack()
    
#₹#₹#₹₹##############
#₹**************************#
def login():
    uname=username.get()
    pwd=password.get()
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      if uname=="hsds.2904@gmail.com" and pwd=="hsds#2904":
       message.set("Login success")
       p2.destroy()
       panel()
       TextOP()
      else:
       message.set("Wrong username or password!!!")
       tk.destroy()
#_____________________________________#
#Loginform()
panel()
TextOP()
tk.mainloop()
con.commit()
con.close()
