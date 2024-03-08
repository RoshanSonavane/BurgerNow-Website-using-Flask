from flask import*
from sqlite3 import*
from flask_mail import*
import pickle
import numpy as np
import warnings
from random import *
warnings.filterwarnings("ignore")

app=Flask(__name__)
app.secret_key="Roshan"

app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=587
app.config["MAIL_USERNAME"]="roshan913637@gmail.com"
app.config["MAIL_PASSWORD"]="ojxnumqitkjlwikw"
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=False

mail=Mail(app)

@app.route("/delete",methods=["GET","POST"])
def delete():
	if "un" in session:
		if request.method=="POST":				
			if "logout" in request.form:
				session.pop("un")
				return redirect(url_for("login"))
			elif "y" in request.form:
				un=session["un"]
				con=None
				try:
					con=connect("repp.db")
					cursor=con.cursor()
					sql="delete from users where un='%s'"
					cursor.execute(sql % (un))
					con.commit()
					return redirect(url_for("thank", m="Your account is succesfully removed."))
				except Exception as e:
					con.rollback()
					print(e)
					return render_template("delete.html",m=e)
				finally:
					if con is not None:
						con.close()
			elif "n" in request.form:
				return render_template("home.html")
			else:
				print("issue")

		else:
			return render_template("delete.html")
	else:
		return redirect(url_for("login"))



@app.route("/veg",methods=["GET","POST"])
def veg():
	if "un" in session:
		if request.method=="POST":
				if "logout" in request.form:
					session.pop("un")
					return redirect(url_for("login"))

				else:
					n=session["un"]
					i=[next(iter(request.form.keys()))][0]
					con=None
					try:
						con=connect("items11.db")
						cursor=con.cursor()
						
						sql2="create table if not exists customer1(nid  integer primary key autoincrement,name varchar(40),id varchar(5),FOREIGN KEY(id) REFERENCES item(id));"
						sql3="insert into customer1(name,id) values('%s','%s'); "
						
						cursor.execute(sql2)
						print(str(n)+" "+str(i))
						cursor.execute(sql3%(n,i))
						con.commit()
						return render_template("veg.html", m="Succesfully added to cart")
					except Exception as e:
						con.rollback()
						print(e)
						return render_template("veg.html",m=e)
						
					finally:
						if con is not None:
							con.close()
		else:
			return render_template("veg.html")

	else:
		return redirect(url_for("login"))
	
@app.route("/bev",methods=["GET","POST"])
def bev():
	if "un" in session:
		if request.method=="POST":
				if "logout" in request.form:
					session.pop("un")
					return redirect(url_for("login"))

				else:
					n=session["un"]
					i=[next(iter(request.form.keys()))][0]
					con=None
					try:
						con=connect("items11.db")
						cursor=con.cursor()
						
						sql2="create table if not exists customer1(nid  integer primary key autoincrement,name varchar(40),id varchar(5),FOREIGN KEY(id) REFERENCES item(id));"
						sql3="insert into customer1(name,id) values('%s','%s'); "
						
						cursor.execute(sql2)
						print(str(n)+" "+str(i))
						cursor.execute(sql3%(n,i))
						con.commit()
						return render_template("bev.html", m="Succesfully added to cart")
					except Exception as e:
						con.rollback()
						print(e)
						return render_template("bev.html",m=e)
						
					finally:
						if con is not None:
							con.close()
		else:
			return render_template("bev.html")

	else:
		return redirect(url_for("login"))
	
	

@app.route("/nveg",methods=["GET","POST"])
def nveg():
	if "un" in session:
		if request.method=="POST":
				if "logout" in request.form:
					session.pop("un")
					return redirect(url_for("login"))

				else:
					n=session["un"]
					i=[next(iter(request.form.keys()))][0]
					con=None
					try:
						con=connect("items11.db")
						cursor=con.cursor()
						
						sql2="create table if not exists customer1(nid  integer primary key autoincrement,name varchar(40),id varchar(5),FOREIGN KEY(id) REFERENCES item(id));"
						sql3="insert into customer1(name,id) values('%s','%s'); "
						
						cursor.execute(sql2)
						print(str(n)+" "+str(i))
						cursor.execute(sql3%(n,i))
						con.commit()
						return render_template("nveg.html", m="Succesfully added to cart")
					except Exception as e:
						con.rollback()
						print(e)
						return render_template("nveg.html",m=e)
						
					finally:
						if con is not None:
							con.close()
		else:
			return render_template("nveg.html")

	else:
		return redirect(url_for("login"))

@app.route("/burger_menu",methods=["GET","POST"])
def burger_menu():
	if request.method=="POST":
		session.pop("un")
		return redirect(url_for("login"))
	if "un" in session:
		return render_template("burger_menu.html",m=session["un"])
	else:
		return redirect(url_for("login"))

@app.route("/customer_menu",methods=["GET","POST"])
def customer_menu():
	if "un" in session:
		if request.method=="POST":
				if "logout" in request.form:
					session.pop("un")
					return redirect(url_for("login"))
				elif "order" in request.form:
	
				

					if "logout" in request.form:
						session.pop("un")
						return redirect(url_for("login"))
					else:
						bname=request.form["bname"]
						print(bname)
						print(request.form)
						a=request.form
						c=[next(iter(request.form.values()))][0]
						
						

						con=None
						try:
							
							newid=randint(1,100)
							bname=request.form["bname"]
							o1=int(a['o1'])
							o2=int(a['o2'])
							o3=int(a['o3'])
							o4=int(a['o4'])
							o5=int(a['o5'])
							o6=int(a['o6'])
							o7=int(a['o7'])
							o8=int(a['o8'])
							o9=int(a['o9'])
							o10=int(a['o10'])
							price=o1+o2+o3+o4+o5+o6+o7+o8+o9+o10
							
							print(str(newid)+str(bname)+str(price))
							con=connect("items11.db")
							cursor=con.cursor()
							
							sql2="insert into customer1(name,id) values('%s','%s'); "
							sql3="insert into item(id,item_name,item_price) values('%s','%s','%s'); "
							
							cursor.execute(sql2%(str(bname),str(newid)))
							cursor.execute(sql3%(str(newid),str(bname),price))
							con.commit()
							return render_template("customer_menu.html", m="Succesfully"+" "+bname+" added to cart")


							
						except Exception as e:
							print("error  = "+str(e))
							return render_template("customer_menu.html", m=e)
						

				
		else:
			return render_template("customer_menu.html")


	else:
		return redirect(url_for("login"))

@app.route("/order",methods=["GET","POST"])
def order():
	if "un" in session:
		if request.method=="POST":
				
				if "logout" in request.form:
					session.pop("un")
					return redirect(url_for("login"))
				elif "Delete" in request.form:
					con=None
					try:
						con=connect("items11.db")
						cursor=con.cursor()
						sql="drop table if exists customer1;"
						cursor.execute(sql)
						con.commit()
						return render_template("order.html", m="All items are removed.")
					except Exception as e:
						con.rollback()
						print(e)
						return render_template("order.html",m=e)
						
					finally:
						if con is not None:
							con.close()
				elif "Purchase" in request.form:
					con=None
					try:
						con=connect("items11.db")
						cursor=con.cursor()
						sql="select sum(item_price) as 'Total' from item join customer1 where item.id=customer1.id ;"
						cursor.execute(sql)
						data=cursor.fetchall()
						info=""
						for d in data:
							
							info=info+str(d[0])
							
						
						return render_template("result.html", m="Total Price of Items are "+str(d[0])+".00/- Rs")
					except Exception as e:
						con.rollback()
						print(e)
						return render_template("order.html",m="First add some items in the cart.")
						
					finally:
						if con is not None:
							con.close()	

			
		else:
					con=None
					try:
						con=connect("items11.db")
						cursor=con.cursor()
						
						sql="select nid as 'Sr.No.', item_name as 'Burger Name', item_price as 'Price' from item join customer1 where item.id=customer1.id order by nid;"
						
						cursor.execute(sql)
						data=cursor.fetchall()
						info=""
						n=""
						o=""
						q=""
						
						for d in data:
							print(d)
							n=n+str(d[0])+"\n"
							o=o+str(d[1])+"\n"
							q=q+str(d[2])+"\n"

						return render_template("order.html",n=n,o=o,q=q)
					except Exception as e:
						con.rollback()
						print(e)
						return render_template("order.html",m="First add some items in the cart.")
						
					finally:
						if con is not None:
							con.close()	



	else:
		return redirect(url_for("login"))

@app.route("/thank",methods=["GET","POST"])
def thank():
	if request.method=="POST":
		session.pop("un")
		return redirect(url_for("login"))
	if "un" in session:
		return render_template("thank.html")
	else:
		return redirect(url_for("login"))


@app.route("/result",methods=["GET","POST"])
def result():
	if request.method=="POST":
		session.pop("un")
		return redirect(url_for("login"))
	if "un" in session:
		return render_template("result.html",m=session["un"])
	else:
		return redirect(url_for("login"))
@app.route("/",methods=["GET","POST"])
def home():
	if request.method=="POST":
		session.pop("un")
		return redirect(url_for("login"))
	if "un" in session:
		return render_template("home.html",m=session["un"])
	else:
		return redirect(url_for("login"))
	

@app.route("/feedback",methods=["GET","POST"])
def feedback():
	if "un" in session:
		if request.method=="POST":
				
				if "logout" in request.form:
					session.pop("un")
					return redirect(url_for("login"))
				elif "sub" in request.form:
					con=None
					try:
						con=connect("fb.db")
						cursor=con.cursor()
						sql="insert into user_feedback values ('%s','%s','%s','%s','%s','%s')"
						username=session["un"]
						email=request.form["email"]
						beautiful=request.form["beautiful"]
						working=request.form["working"] 
						useful=request.form["useful"]
						suggestion=request.form["suggestion"]
						print(email)
						cursor.execute(sql%(username,email,beautiful,working,useful,suggestion))
						con.commit()
						subject="Burger Now Web app feedback"
						sender="roshan913637@gmail.com"
						recipients=[email]
						message=Message(subject,sender=sender,recipients=recipients)
						message.body="username :"+username+"\n"+"email id :"+email+"\n"+"This app is beautiful? :"+beautiful+"\n"+"This app is working? :"+working+"\n""This app is useful? :"+useful+"\n""Suggestion :"+suggestion+"\n""Thank you for your feedback."
						mail.send(message)
						return render_template("feedback.html", m="Succesfully Feedback is submitted and feedback report is sent on given email id.")
					except Exception as e:
						con.rollback()
						print(e)
						return render_template("feedback.html",m="Already feedback is given.")
					
						
					finally:
						if con is not None:
							con.close()

		else:
			return render_template("feedback.html")

	else:
		return redirect(url_for("login"))
@app.route("/login",methods=["GET","POST"])
def login():
	if "un" in session:
		return redirect(url_for("login"))
	if request.method=="POST":
		un=request.form["un"]
		pw=request.form["pw"]
		con=None
		try:
			con=connect("repp.db")
			cursor=con.cursor()
			sql="select*from users where un= '%s' and pw='%s'"
			cursor.execute(sql % (un,pw))
			data=cursor.fetchall()
			if len(data)==0:
				return render_template("login.html",m="invalid username / password ")
			else:
				session["un"]=un
				return redirect(url_for("home"))
		except Exception as e:
			return render_template("signup.html",m="issue"+str(e))
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
	if "un" in session:
		return redirect(url_for("home"))
	if request.method=="POST":
		un=request.form["un"]
		pw1=request.form["pw1"]
		pw2=request.form["pw2"]
		if len(un)<2:
			return render_template("signup.html",m="user name aleast contain 2 alphabets.")
		elif len(pw1)<5:
			return render_template("signup.html",m="password should contain atleast 5 characters.")

		elif pw1==pw2:
			con=None
			try:
				con=connect("repp.db")
				cursor=con.cursor()
				sql="insert into users values('%s','%s')"
				cursor.execute(sql % (un,pw1))
				con.commit()
				return redirect(url_for("login"))
			except Exception as e:
				con.rollback()
				print(e)
				return render_template("signup.html",m="user already exists")
			finally:
				if con is not None:
					con.close()
		else:
			return render_template("signup.html",m="password did not match")
	else:
		return render_template("signup.html")

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)
