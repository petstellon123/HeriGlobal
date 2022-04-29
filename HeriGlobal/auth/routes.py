from flask import Blueprint, flash, redirect, url_for, render_template, request
from HeriGlobal import login_manager
from HeriGlobal.model import User, db
from flask_login import login_user, logout_user

auth_bp = Blueprint("auth_bp", __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/', methods=["GET", "POST"])
@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form[ 'password' ]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin_bp.dashboard'))
        flash("Invalid username or password")
        return redirect(url_for('auth_bp.login'))
    return render_template("/auth/boss_login.html", title='HERI GLOBAL MERCHANT')

@auth_bp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        name = request.form[ 'name' ].upper()
        email = request.form[ 'email' ]
        password = request.form[ 'password' ]

        #check if user exit
        user = User.query.filter((User.username==username)|(User.email==email)).first()
        admin_created = User.query.filter_by(is_admin=True).first()
        if user:
            flash("A user with this email or username already exit.")
            return redirect(url_for('auth_bp.signup'))
        if admin_created:
            flash("An admin has been created already.")
            return redirect(url_for('auth_bp.signup'))
        new_user = User(username, name, email, "ACTIVE")
        new_user.set_password(password)
        new_user.is_admin = True
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('admin_bp.dashboard'))
    return render_template("/auth/register.html", title='HERI GLOBAL MERCHANT')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    flash('you must be logged in to view that page')
    return redirect(url_for('auth_bp.login'))