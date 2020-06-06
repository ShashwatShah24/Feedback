import sqlite3  
  
con = sqlite3.connect("feedback.db")  
print("Database opened successfully")  
  
con.execute("create table tab01 (Name TEXT NOT NULL, Age TEXT  NOT NULL,Husband TEXT NOT NULL,Address TEXT NOT NULL, Phone TEXT NOT NULL,Date TEXT NOT NULL,Fees TEXT NOT NULL,Admission TEXT NOT NULL,Diagnosis TEXT NOT NULL,Remark TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()