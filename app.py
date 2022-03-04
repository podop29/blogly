from crypt import methods
from flask import Flask, request, render_template, flash, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "OOooOOOoOOOoo000"


connect_db(app)
db.create_all()


@app.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)


@app.route('/create-user')
def create_user():
    return render_template("new-user.html")

@app.route('/create-user', methods=["POST"])
def create_user_post():
    "Gets all info for the new user"
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    "Creates new user, adds to staging area, and commits"
    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url or None)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')


@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user-detail.html",user=user)



"edit"

@app.route("/user/<int:user_id>/edit")
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit-user.html", user=user)

@app.route("/user/<int:user_id>/edit", methods=["POST"])
def edit_user_post(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.img_url = request.form["img_url"]

    db.session.add(user)
    db.session.commit()

    return render_template("edit-user.html", user=user)

"delete"
@app.route("/user/<int:user_id>/delete")
def delete_user(user_id):
    User.query.filter_by(id = user_id).delete()
    db.session.commit()
    
    return redirect('/')

