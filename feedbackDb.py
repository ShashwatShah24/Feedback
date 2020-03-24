import sqlite3  
  
con = sqlite3.connect("feedback.db")  
print("Database opened successfully")  
  
con.execute("create table tab01 (Name TEXT NOT NULL, id TEXT  NOT NULL,TOOL TEXT NOT NULL,feedback TEXT NOT NULL,Email TEXT NOT NULL,Incase TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()