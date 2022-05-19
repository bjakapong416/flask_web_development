import sqlite3
from flask import Flask , render_template , request
app = Flask(__name__)



def get_db_connection():
    conn = sqlite3.connect('../model/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/test')
def database():
    print("Database")
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    # conn.close()
    print(posts)
    # print(posts)
    return render_template("about.html", data = {"name":"admin"})


# @app.route('/')
# def index():
#     return "<h1> Hello world!</h1>"


@app.route('/')
def index():
    #Params 
    # name = "World !"
    # return render_template("index.html",myname = name)

    # Dictionary
    data = { "name": "BUU" , "Location":"BUU"}
    return render_template("index.html",mydata = data)


@app.route('/about')
def about():
    # return "<h1> เกี่ยวกับ </h1>"
    return render_template("about.html")


@app.route('/stock')
def stock():
    products = ["แก้วน้ำ" , "ไวนิล", "พลาสติก"]
    return render_template("stock.html",myproduct = products)

# Dynamic Route
@app.route('/user/<name>')
def user(name):
    return f"<h1> สวัสดีคุณ {name} </h1>"

@app.route('/register')
def register():
    username = "admin"
    password = "admin"
    return render_template("register.html")


@app.route('/sendData')
def signup():
    uname = request.args.get('username')
    pwd = request.args.get('password')
    return render_template("thankyou.html", data = {"uname": uname ,"pwd":pwd})



if __name__=="__main__":
    app.run(debug=True)