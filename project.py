rom flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__, template_folder = '/home/ubuntu/project_templates/')

@app.route('/')
def home():
   return render_template('welcome.html')

@app.route('/reserve')
def new_registration():
   return render_template('reservation.html')


@app.route('/confirmation',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         FirstName = request.form['nm']
         LastName = request.form['ln']
         Email = request.form['email']
         Phone = request.form['phone']
         Origins = request.form['orig']
         Destination = request.form['dest']
         Date = request.form['date']

         with sql.connect("/home/ubuntu/final_project/flights.db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO flights (FirstName,LastName,Email,Phone,Origins,Destination,Date) VALUES ('{0}','{1}','{2}','{3}','{4}',{5}','{6}')".format(FirstName,LastName,Email,Phone,Origins,Destination,Date)
            cur.execute(cmd)

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("confirmation.html",nm = FirstName, ln=LastName, email=Email, phone=Phone, orig=Origins, dest=Destination, date=Date)
         con.close()

@app.route('/list')
def information():
   con = sql.connect("/home/ubuntu/final_project/flights.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from flights")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
