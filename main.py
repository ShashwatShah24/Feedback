from flask import *  
import sqlite3  
  
app = Flask(__name__)   

@app.route("/")  
def index():  
    return render_template("feedback.html")

@app.route("/savedetails121",methods = ["POST"])  
def saveDetails121():
	msg="msg"
	name = request.form["Name"]
	print(name)
	id1 = request.form["id1"]
	print(id1)
	Email = request.form["Email"]
	print(Email)
	tool = request.form.get("tools", None)
	print(tool)
	feedback = request.form["feedback"]
	print(feedback)
	incase = request.form["incase"]
	print(incase)
	with sqlite3.connect("feedback.db") as con:
		cur = con.cursor()
		cur.execute("INSERT into tab01 (Name,id,TOOL,feedback,Email,Incase) values (?,?,?,?,?,?)",(name,id1,tool,feedback,Email,incase))
		print("execute")
		con.commit()
		print("commit")
		msg="feedback success"
		return render_template("success01.html",msg=msg)






if __name__ == "__main__":
	app.run(host='127.0.0.1', port=7070)  