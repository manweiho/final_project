from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector as sql
app = Flask(__name__, template_folder = '/home/ubuntu/project_templates/')
app.secret_key = 'your_secret_key'

USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            # Store the username in a session
            session['username'] = username
            return redirect(url_for('information'))
        else:
            return "Invalid username or password"
    return render_template('login.html')

@app.route('/')
def home():
   if 'username' in session:
     session.pop('username',None)
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
         Origin = request.form['orig']
         Destination = request.form['dest']
         Date = request.form['date']
         DepartureTime = request.form['time']

         with sql.connect(host="localhost", user="final", password="2807", database="flights_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO flights (FirstName,LastName,Email,Phone,Origin,Destination,Date,DepartureTime) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(FirstName,LastName,Email,Ph>
            cur.execute(cmd)
            
            con.commit()
            msg = "has been sucessfully made"

            cur.execute("SELECT LAST_INSERT_ID()")
            id = cur.fetchone()[0]
      except:
         con.rollback()
         msg = "had an error. Please try again or contact customer service"

      finally:
         return render_template("confirmation.html",id=id,nm = FirstName, ln=LastName, email=Email, phone=Phone, orig=Origin, dest=Destination, date=Date, time=DepartureTime,msg=msg)
         con.close()

@app.route('/list')
def information():
  if 'username' in session:    
    with sql.connect(host="localhost", user="final", password="2807", database="flights_db") as conn:
      cur = conn.cursor()
      cur.execute("select * from flights")
      rows = cur.fetchall()
 
    return render_template("list.html",rows = rows)

  else:
    return redirect(url_for('login'))
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        id_query = request.form['id']
        first_name_query = request.form['first_name']
        last_name_query = request.form['last_name']

        with sql.connect(host="localhost", user="final", password="2807", database="flights_db") as con:
            cur = con.cursor()

            # Search by ID, First Name, and Last Name
            cur.execute("SELECT * FROM flights WHERE FlightID = %s AND FirstName = %s AND LastName = %s", (id_query, first_name_query, last_name_query))

            rows = cur.fetchall()

        con.close()
        return render_template("search_results.html", rows=rows)

    return render_template("search.html")

if __name__ == '__main__':
   app.run(debug = True)

