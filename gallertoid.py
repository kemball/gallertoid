from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    if app.debug:
        return "DEBUG IS ON. PANIC PANIC PANIC"
    return "Hello World"



if __name__=="__main__":
    app.run()
