from flask import Blueprint, url_for, request, redirect, render_template, flash
from flask_login import login_user, login_required, current_user, logout_user
from HeriGlobal.model import db, User, Products
from datetime import datetime as dt

admin_bp = Blueprint("admin_bp", __name__, template_folder='templates', static_folder='static')


#this route create sales rep account
@admin_bp.route("/create_sales_rep", methods=["GET", "POST"])
@login_required
def create_sales_rep():
    if current_user.is_admin:
        if request.method == "POST":
            username = request.form[ 'username' ]
            name = request.form[ 'name' ].upper()
            email = request.form[ 'email' ]
            password = request.form[ 'password' ]

            # check if user exit
            user = User.query.filter((User.username == username) | (User.email == email)).first()
            if user:
                flash("A user with this email or username already exit.", 'red')
                return redirect(url_for('admin_bp.dashboard'))
            new_user = User(username, name, email, "ACTIVE")
            new_user.set_password(password)
            new_user.is_admin = False
            db.session.add(new_user)
            db.session.commit()
            flash(f'{name} account created successfully.', 'green')
            return redirect(url_for('admin_bp.dashboard'))
        return redirect(url_for('admin_bp.dashboard'))
    flash("Access Denied.")
    return redirect(url_for('auth_bp.logout'))

#this route block or delete sales rep
@admin_bp.route("/block_or_delete_rep", methods=["GET", "POST"])
@login_required
def block_or_delete_rep():
    return "block_or_delete_rep"

#this route create admin dashboard
@admin_bp.route('/dashboard', methods=["POST", "GET"])
@login_required
def dashboard():
    if current_user.is_admin:
        date = dt.now()
        sales_reps = User.query.filter_by(is_admin=False).all()
        items = Products.query.all()
        return render_template('/admin/dashboard.html',
                               date=date,
                               reps=sales_reps,
                               item = items,
                               title="HERI GLOBAL MERCHANT | DASHBOARD")

    flash("Invalid username or password")
    return redirect(url_for('auth_bp.logout'))

#this route edit sales rep profile
@admin_bp.route('/edit_sales_profile', methods=["GET", "POST"])
@login_required
def edit_sales_profile():
    if current_user.is_admin:
        if request.args:
            id = request.args.get('id')
            user = User.query.filter_by(id=id).first()
            if request.args.get('action') == "activate":
                user.status = "ACTIVE"
                db.session.add(user)
                db.session.commit()
                flash(f"{user.name} account re-activated successfully.", "green")
                return redirect(url_for('admin_bp.dashboard'))
            elif request.args.get('action') == "block":
                user.status = "BLOCKED"
                db.session.add(user)
                db.session.commit()
                flash(f"{user.name} account blocked successfully.", "green")
                return redirect(url_for('admin_bp.dashboard'))
            elif request.args.get('action') == "delete":
                db.session.delete(user)
                db.session.commit()
                flash(f"{user.name} account deleted successfully.", "green")
                return redirect(url_for('admin_bp.dashboard'))
            else:
                user.set_password(user.username)
                db.session.add(user)
                db.session.commit()
                flash(f"{user.name} account password reset successfully.\nNew password: {user.username}", "green")
                return redirect(url_for('admin_bp.dashboard'))
        return redirect(url_for('admin_bp.dashboard'))
    return redirect(url_for('auth_bp.logout'))

#this route get stock report from api
@admin_bp.route('/stock_report', methods=["GET", "POST"])
@login_required
def stock_report():
    return 'stock report'

#this route create new stock
@admin_bp.route('/register_stock', methods=["GET", "POST"])
@login_required
def register_stock():
    if current_user.is_admin:
        if request.method == "POST":
            item = request.form['name'].upper()
            has_slate = request.form[ 'has_slate' ]
            qty = request.form[ 'quantity' ]
            price = request.form['unit_price']

            check_item = Products.query.filter_by(name = item).first()
            if check_item:
                flash(f'{item} already registered.', 'red')
                return redirect(url_for('admin_bp.dashboard'))
            new_item = Products(item, qty, price)
            if has_slate == 'True':
                new_item.has_slate = True
                new_item.slate = request.form['num_slate']
            else:
                new_item.has_slate = False
            db.session.add(new_item)
            db.session.commit()
            flash(f"{item} registered sucessfully.", 'green')
            return redirect(url_for('admin_bp.dashboard'))
        return redirect(url_for('admin_bp.dashboard'))
    return redirect(url_for('auth_bp.logout'))

#this route check sales transaction by ref, date and today
@admin_bp.route('/sales_trans', methods=["GET", "POST"])
@login_required
def sales_trans():
    return "sales trans ref"

#this route create debtors account
@admin_bp.route('/create_debtors', methods=["GET", "POST"])
@login_required
def create_debtors():
    return "create debtors"

#this route create debtors statement of account
@admin_bp.route('/debtors_statement', methods=["GET", "POST"])
@login_required
def debtors_statement():
    return 'debtors_statement'

#this route make repayment for debtors
@admin_bp.route('/repayment', methods=["GET", "POST"])
@login_required
def repayment():
    return "repayment"






