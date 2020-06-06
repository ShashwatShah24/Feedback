from flask import *  
import sqlite3  
  
app = Flask(__name__)   

@app.route("/")  
def index():  
    return render_template("success01.html")

@app.route("/feed1")  
def feed1():  
    return render_template("feedback.html")

@app.route("/feed2")  
def feed2():  
    return render_template("feedback2.html")

@app.route("/savedetails121",methods = ["POST"])  
def saveDetails121():
	msg="msg"
	name = request.form["Name"]
	print(name)
	Age = request.form["Age"]
	print(Age)
	Husband = request.form["Husband"]
	print(Husband)
	Address = request.form["Address"]
	print(Address)
	Phone = request.form["Phone"]
	print(Phone)
	Date = request.form["Date"]
	print(Date)
	Fees = request.form["Fees"]
	print(Fees)
	Admission = request.form.get("Admission", None)
	print(Admission)
	Diagnosis = request.form["Diagnosis"]
	print(Diagnosis)
	Remark = request.form["Remark"]
	print(Remark)
	with sqlite3.connect("feedback.db") as con:
		cur = con.cursor()
		cur.execute("INSERT into tab01 (Name,Age,Husband,Address,Phone,Date,Fees,Admission,Diagnosis,Remark) values (?,?,?,?,?,?,?,?,?,?)",(name,Age,Husband,Address,Phone,Date,Fees,Admission,Diagnosis,Remark))
		print("execute")
		con.commit()
		print("commit")
		msg="feedback success"
		return render_template("success01.html",msg=msg)

@app.route("/savedetails122",methods = ["POST"])  
def saveDetails122():
	msg="msg"
	name = request.form["Name"]
	print(name)
	Age = request.form["Age"]
	print(Age)
	Husband = request.form["Husband"]
	print(Husband)
	Address = request.form["Address"]
	print(Address)
	Phone = request.form["Phone"]
	print(Phone)
	Date = request.form["Date"]
	print(Date)
	Fees = request.form["Fees"]
	print(Fees)
	Admission = request.form.get("Admission", None)
	print(Admission)
	lmp = request.form["LMP"]
	print(lmp)
	edd = request.form["EDD"]
	print(edd)
	g_or_p = request.form["G_OR_P"]
	print(g_or_p)
	Remark = request.form["Remark"]
	print(Remark)
	with sqlite3.connect("feedback.db") as con:
		cur = con.cursor()
		cur.execute("INSERT into tab02 (Name,Age,Husband,Address,Phone,Date,Fees,Admission,LMP,EDD,G_OR_P,Remark) values (?,?,?,?,?,?,?,?,?,?,?,?)",(name,Age,Husband,Address,Phone,Date,Fees,Admission,lmp,edd,g_or_p,Remark))
		print("execute")
		con.commit()
		print("commit")
		msg="feedback success"
		return render_template("success01.html",msg=msg)




if __name__ == "__main__":
	app.run(host='127.0.0.1', port=7075,threaded=True)  