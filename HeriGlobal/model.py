from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime as dt


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=True)
    status = db.Column(db.String, nullable=False)

    def __init__(self, username, name, email, status):
        self.username = username
        self.name = name
        self.email = email
        self.status = status

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.username)

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    has_slate = db.Column(db.Boolean, nullable=True)
    slate = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Float, unique=False, nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    available = db.Column(db.Boolean, nullable=True, default=True)

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return "<Products {}>".format(self.name)

class StockMonitor:
    __tablename__ = 'stockmonitor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=False)
    opening_bal = db.Column(db.Float, nullable=True)
    received = db.Column(db.Float, unique=False, nullable=True)
    sales = db.Column(db.Float, unique=False, nullable=True)
    closing_bal = db.Column(db.Float, nullable=True)
    date = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name, opening_bal, received, sales, closing_bal, date):
        self.name = name
        self.opening_bal = opening_bal
        self.received = received
        self.sales = sales
        self.closing_bal = closing_bal
        self.date = date

    def __repr__(self):
        return "<StockMonitor {}>".format(self.name)


class ReceiveStock:
    __tablename__ = 'receivestock'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=False)
    received = db.Column(db.Float, unique=False, nullable=False)
    bal_before = db.Column(db.Float, nullable=False)
    bal_after = db.Column(db.Float, nullable=False)
    date = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name, received, bal_before, bal_after, date):
        self.name = name
        self.received = received
        self.bal_after = bal_after
        self.bal_before = bal_before
        self.date = date

    def __repr__(self):
        return "<ReceiveStock {}>".format(self.name)

class SalesTransaction:
    __tablename__  = 'salestransaction'
    id = db.Column(db.Integer, primary_key=True)
    ref = db.Column(db.String(200), nullable=False, unique=True)
    cus_name = db.Column(db.String(200), nullable=False, unique=False)
    item_name = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(100), nullable=True, default="COMPLETED")
    date_time = db.Column(db.DateTime, nullable=False, default=dt.now())
    date = db.Column(db.String(20), nullable=False)
    sales_rep = db.Column(db.String(100), nullable=False)
    payment_mode = db.Column(db.String(50), nullable=False)

    def __init__(self, ref, cus_name, item_name, quantity, price, total, date, sales_rep, payment_mode):
        self.ref = ref
        self.cus_name = cus_name
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.total = total
        self.date = date
        self.sales_rep = sales_rep
        self.payment_mode = payment_mode

    def __repr__(self):
        return "<SalesTransaction {}>".format(self.ref)


class DebtorAccount:
    __tablename__ = 'debtoraccount'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False, unique=True)
    cus_name = db.Column(db.String(200), nullable=False, unique=False)
    phone = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, cus_name, phone, amount):
        self.user_id = user_id
        self.cus_name = cus_name
        self.phone = phone
        self.amount = amount

    def __repr__(self):
        return "<DebtorAccount {}>".format(self.user_id)


class DebtorTransaction:
    __tablename__ = 'debtortransaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False, unique=False)
    cus_name = db.Column(db.String(200), nullable=False, unique=False)
    trans_type = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    sale_ref = db.Column(db.String(100), nullable=False)
    sales_rep = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=dt.now())
    date = db.Column(db.String(20), nullable=False)
    prev_bal = db.Column(db.Float, nullable=False)
    new_bal = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, cus_name, trans_type, amount, sale_ref, sales_rep, date, prev_bal, new_bal):
        self.user_id = user_id
        self.cus_name = cus_name
        self.trans_type = trans_type
        self.amount = amount
        self.sale_ref = sale_ref
        self.sales_rep = sales_rep
        self.date = date
        self.prev_bal = prev_bal
        self.new_bal = new_bal

    def __repr__(self):
        return "<DebtorTransaction {}>".format(self.user_id)





