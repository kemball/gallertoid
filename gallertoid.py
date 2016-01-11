from flask import Flask,send_from_directory,render_template
from flask import request,redirect,flash,url_for
from flask.ext.login import LoginManager,login_required,login_user,logout_user
from database import db_session,init_db
from users import Galluser
login_manager = LoginManager()

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'this is a very secret key'

login_manager.init_app(app)
login_manager.login_view="login"
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(id):
    return Galluser.query.filter(Galluser.id==id).first()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<username>')
@login_required
def showuser(username):
    return render_template('user.html')


@app.route('/<path:resource>')
def serve_static(resource):
    return send_from_directory('static/',resource)



from scrypt import hash
@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            realuser = Galluser.query.filter_by(username=username).first()
            if realuser:
                userhash = hash(realuser.nonce,password.encode('utf-8'))
                if userhash == realuser.hash:
                    login_user(realuser)
                    #for fancyness, should take 'next' parameter etc etc
                    #validate it etc etc
                    return redirect(url_for("showuser",username=realuser.username))
    flash("Login failed")
    return render_template("login.html")
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



from os import urandom
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        passwordver = request.form['passwordverify']
        if password != passwordver or not username or not password:
            #there should be javascript to let someone know this
            # but just in case
            flash("Your password and verification password don't match")
            return redirect(url_for('register'))
        if Galluser.query.filter(Galluser.username == username).first():
            #there's another user with that username
            #there should be javascript to let someone know this
            flash("Try another username,that one is taken")
            return redirect(url_for('register'))
        nonce = urandom(64)
        userhash = hash(nonce,password.encode('utf-8'))
        user = Galluser(username,email,nonce,userhash)
        db_session.add(user)
        db_session.commit()
        flash("Welcome! Test-drive your credentials here")
        return redirect(url_for("login"))


if __name__=="__main__":
    app.run()
