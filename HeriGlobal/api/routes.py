from flask import Blueprint
from HeriGlobal.model import db, User, SalesTransaction, StockMonitor, DebtorAccount, DebtorTransaction

api_bp = Blueprint("api_bp", __name__, template_folder='templates', static_folder='static')

#this route gets login details and confirm if user is valid
@api_bp.route('/login', methods=["POST"])
def login():
    return "login api worked"

#this route check sales transaction by ref, date and today
@api_bp.route('/sales_transaction', methods=["POST"])
def sales_transaction():
    return "sales trans ref"

#this route get the daily stock report
@api_bp.route("/available_stock", methods=["POST"])
def available_stock():
    return "available stock"

#this route create debtors account
@api_bp.route('/create_debtors', methods=["POST"])
def create_debtors():
    return "create debtors"

#this route create debtors statement of account
@api_bp.route('/debtors_statement', methods=["POST"])
def debtors_statement():
    return 'debtors_statement'

#this route make repayment for debtors
@api_bp.route('/repayment', methods=["POST"])
def repayment():
    return "repayment"
