from flask import Flask,send_from_directory,render_template,request
app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<path:resource>')
def serve_static(resource):
    return send_from_directory('static/',resource)



@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == "GET":
        return "This will show you the login box one day"
    elif request.method == "POST":
        return "You logged in, probably?"


if __name__=="__main__":
    app.run()
