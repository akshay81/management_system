from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3


def f1():
	root.withdraw()
	add_page.deiconify()

def f2():
	add_page.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	view_page.deiconify()
	view_page_data.delete(1.0, END)
	con = None
	try:
		con = connect("akshay.csv")
		sql = "select * from student"
		cursor = con.cursor()
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "rno : " + str(d[0]) + " " + " name : " + str(d[1]) + " " + "marks : " + str(d[2]) + "\n"
		view_page_data.insert(INSERT, info)
	except Exception as e:
		showerror("issue", e)
	finally:
		if con is not None:
			con.close()

	
	
def f4():
	view_page.withdraw()
	root.deiconify()

def f5():
	
	con = None
	try:
		con = connect("akshay.csv")
		sql = "insert into student values('%d', '%s', '%d')"
		cursor = con.cursor()
		rno = int(add_page_entrno.get())
		name = add_page_entname.get()
		marks = int(add_page_entmarks.get())
		if rno <= 0:
			showerror("Error", "Enter Valid Rno")	
		elif (name.isalpha()) == False or len(name) < 2:
			showerror("Error", "Enter Valid Name")
		elif marks < 0 or marks > 100:		
			showerror("Error", "Enter Valid Marks")	
		else:
			cursor.execute(sql % (rno, name, marks))
			con.commit()
			showinfo("Success", "record added")
	except ValueError as e:
		showerror("Error", "Enter Valid Rno & Valid Marks")
	except NameError as e:
		showerror("Error", "Enter Valid Name")
	except IntegrityError as e:
		showerror("Error", "Roll no Already exists")
	except Exception as e:
		showerror("Failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f6():
	upd_page.withdraw()
	root.deiconify()

def f7():
	root.withdraw()
	del_page.deiconify()

def f8():
	del_page.withdraw()
	root.deiconify()
def f9():
	root.withdraw()
	upd_page.deiconify()
	
def f10():
	con = None
	try:
		con = connect("akshay.csv")
		print("connected")
		sql = "update student set name ='%s', marks='%d' where rno='%d' "
		cursor = con.cursor()
		
		rno = int(upd_page_entrno.get())
		name = upd_page_entname.get()
		marks = int(upd_page_entmarks.get())
		if rno <= 0:
			showerror("Error", "Enter Valid Rno")
		elif (name.isalpha()) == False or len(name) < 2:
			showerror("Error", "Enter Valid Name")
		elif marks < 0 or marks > 100:
			showerror("Error", "Enter Valid Marks")
		else:
			cursor.execute(sql % (name, marks, rno))
			data = cursor.fetchall()
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Sucess","Record Updated")
			else:
				showwarning("Warning","Record does not exist")
	except ValueError as e:
		showerror("Error", "Enter Valid Rno & Valid Marks")
	except NameError as e:
		showerror("Error", "Enter Valid Name")
	except Exception as e:
		print("issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("disconnected")

def f11():
	con = None
	try:
		con = connect("akshay.csv")
		print("connected")
		sql = "delete from student where rno='%d' "
		
		cursor = con.cursor()
		rno = int(del_page_entrno.get())

		cursor.execute(sql % (rno))
		data = cursor.fetchall()
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success","Record Deleted")
		else:
			showwarning("Error","record does not exists")
	except ValueError as e:
		showerror("Error", "Enter Valid Rno & Valid Marks")
	except NameError as e:
		showerror("Error", "Enter Valid Name")
	except Exception as e:
		print("issues", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("disconnected")
	
def f12():
	con = sqlite3.connect("akshay.csv")
	data = pd.read_sql_query("select name,marks from student;",con)
	#print(data)

	name = data['name'].tolist()
	marks = data['marks'].tolist()
	x = np.arange(len(name))

	plt.bar(name, marks, width=0.25, color=['red', 'green', 'blue'])
	plt.xticks(name)
	plt.xlabel("Name")
	plt.ylabel("Marks")
	plt.title("Batch Information")

	plt.show()
		
#S.M.S Page
root = Tk()
root.title("S.M.S")
root.geometry("700x700+350+100")	


try:
	web_add = "https://www.brainyquote.com/quote_of_the_day"
	res = requests.get(web_add)
	#print(res)
		
	data = bs4.BeautifulSoup(res.text, "html.parser")		#BeautifulSoup is used to get the data out of HTML, XML page
	#print(data)

	info = data.find("img", {"class":"p-qotd"})
	#print(info)

	quote = info['alt']
	#print(quote)
		
	T = Text(root, height=3, width=65)
	T.place(x=100,y=450)
	
	T.insert(END, quote)						#to insert the quote from above where we are fetching the code from i.e. info['alt']
	T.configure(state='disabled')					#it makes the text permaenant


	web_address = "https://ipinfo.io/"
	res1 = requests.get(web_address)
	#print(res)

	data = res1.json()
	#print(data)

	city_name = data['city']
	#print("City name : ", city_name)

	T = Text(root, height=2, width=15,font=('arial',12,'bold'))
	T.place(x=130,y=400)
	
	T.insert(END, city_name)						
	T.configure(state='disabled')

	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city_name 
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	web_add = a1 + a2 + a3
	res = requests.get(web_add)
	print(res)
	
	data = res.json()
	print(data)
	
	#a1 = data['main']
	#t = a1['temp']
	#print("Temp = ", t)

	at = data['main']['temp']
	print("another temp= ",at)

	
	text2= Text(root,width=19,height=2,font=('arial',12,'bold'))
	
	text2.place(x=400,y=400)
	
	text2.insert(END,at)
		



except Exception as e:
	print("issues", e) 



btnAdd = Button(root, text="Add", width=20,  font=('arial', 20, 'bold'), command=f1)

btnView = Button(root, text="View", width=20, font=('arial', 20, 'bold'), command=f3)

btnUpdate = Button(root, text="Update", width=20, font=('arial', 20, 'bold'), command=f9)

btnDelete = Button(root, text="Delete", width=20, font=('arial', 20, 'bold'), command=f7)

btnCharts = Button(root, text="Charts", width=20, font=('arial', 20, 'bold'), command=f12)

lblLocation = Label(root, text="Location:", font=('arial', 18, 'bold'))

lblTemp = Label(root, text="Temp:", font=('arial', 18, 'bold'))

lblQOTD = Label(root, text="QOTD:", font=('arial', 18, 'bold'))


btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnCharts.pack(pady=10)
lblLocation.place(x=10, y=400)
lblTemp.place(x=300, y=400)
lblQOTD.place(x=10, y=450)

#Add Student Page

add_page = Toplevel(root)
add_page.title("Add Student")
add_page.geometry("500x500+350+100")
	

add_page_lblrno = Label(add_page, text="enter rno : ", font=('arial', 20, 'bold' ))
add_page_lblrno.pack(pady=10)
add_page_entrno = Entry(add_page, bd=5, font=('arial', 20, 'bold' ))
add_page_entrno.pack(pady=10)
add_page_lblname = Label(add_page, text="enter name : ", font=('arial', 20, 'bold' ))
add_page_lblname.pack(pady=10)
add_page_entname = Entry(add_page, bd=5, font=('arial', 20, 'bold' ))
add_page_entname.pack(pady=10)
add_page_lblmarks = Label(add_page, text="enter marks : ", font=('arial', 20, 'bold' ))
add_page_lblmarks.pack(pady=10)
add_page_entmarks = Entry(add_page, bd=5, font=('arial', 20, 'bold' ))
add_page_entmarks.pack(pady=10)

add_page_btnsave = Button(add_page, text="Save", width=5, font=('arial', 20, 'bold' ), command=f5)
add_page_btnsave.pack(pady=10)

add_page_btnback = Button(add_page, text="Back", width=5, font=('arial', 20, 'bold' ), command=f2)
add_page_btnback.pack(pady=10)
add_page.withdraw()

#Adding View Page

view_page = Toplevel(root)
view_page.title("View Student")
view_page.geometry("500x500+350+100")


view_page_data = ScrolledText(view_page, width=28, height=10, font=('arial', 20, 'bold'))
view_page_btnback = Button(view_page, text="Back", width=5, font=('arial', 20, 'bold'), command=f4)

view_page_data.pack(pady=20)
view_page_btnback.pack(pady=20)
view_page.withdraw()

#Adding a new page Update Student

upd_page = Toplevel(root)
upd_page.title("Update Student")
upd_page.geometry("500x500+300+150")


upd_page_lblrno = Label(upd_page, text="enter rno : ", font=('arial', 20, 'bold' ))
upd_page_lblrno.pack(pady=10)
upd_page_entrno = Entry(upd_page, bd=5, font=('arial', 20, 'bold' ))
upd_page_entrno.pack(pady=10)
upd_page_lblname = Label(upd_page, text="enter name : ", font=('arial', 20, 'bold' ))
upd_page_lblname.pack(pady=10)
upd_page_entname = Entry(upd_page, bd=5, font=('arial', 20, 'bold' ))
upd_page_entname.pack(pady=10)
upd_page_lblmarks = Label(upd_page, text="enter marks : ", font=('arial', 20, 'bold' ))
upd_page_lblmarks.pack(pady=10)
upd_page_entmarks = Entry(upd_page, bd=5, font=('arial', 20, 'bold' ))
upd_page_entmarks.pack(pady=10)

upd_page_btnsave = Button(upd_page, text="Save", width=5, font=('arial', 20, 'bold' ), command=f10)
upd_page_btnsave.pack(pady=10)

upd_page_btnback = Button(upd_page, text="Back", width=5, font=('arial', 20, 'bold' ), command=f6)
upd_page_btnback.pack(pady=10)
upd_page.withdraw()

#Adding a new page Delete Student

del_page = Toplevel(root)
del_page.title("Delete Student")
del_page.geometry("500x500+350+100")


del_page_lblrno = Label(del_page, text="Enter Rno : ", font=('arial', 20, 'bold'))
del_page_entrno = Entry(del_page, bd=5,  font=('arial', 20, 'bold' ))
del_page_btnsave = Button(del_page, text="Save", width=5,  font=('arial', 20, 'bold' ), command=f11)
del_page_btnback = Button(del_page, text="Back", width=5, font=('arial', 20, 'bold'), command=f8)


del_page_lblrno.pack(pady=20)
del_page_entrno.pack(pady=20)
del_page_btnsave.pack(pady=20)
del_page_btnback.pack(pady=10)
del_page.withdraw()

root.mainloop()