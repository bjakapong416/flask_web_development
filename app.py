from flask import Flask , render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#     return "<h1> Hello world!</h1>"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return "<h1> เกี่ยวกับ </h1>"


@app.route('/stock')
def stock():
    return "<h1> สินค้า </h1>"

# Dynamic Route
@app.route('/user/<name>')
def user(name):
    return f"<h1> สวัสดีคุณ {name} </h1>"



if __name__=="__main__":
    app.run(debug=True)