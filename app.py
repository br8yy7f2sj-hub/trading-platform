#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt, os
from datetime import datetime, timedelta

app = Flask(**name**)
app.config[‘SECRET_KEY’] = os.environ.get(‘SECRET_KEY’, ‘najd-secret’)
app.config[‘SQLALCHEMY_DATABASE_URI’] = os.environ.get(‘DATABASE_URL’, ‘sqlite:///najd.db’)
app.config[‘SQLALCHEMY_TRACK_MODIFICATIONS’] = False

CORS(app)
db = SQLAlchemy(app)

class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
password = db.Column(db.String(200), nullable=False)
balance = db.Column(db.Float, default=10000)
invested = db.Column(db.Float, default=0)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
trades = db.relationship(‘Trade’, backref=‘user’, lazy=True)
def set_password(self, password):
self.password = generate_password_hash(password)
def check_password(self, password):
return check_password_hash(self.password, password)

class Trade(db.Model):
id = db.Column(db.Integer, primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey(‘user.id’), nullable=False)
symbol = db.Column(db.String(20), nullable=False)
action = db.Column(db.String(10), nullable=False)
price = db.Column(db.Float, nullable=False)
amount = db.Column(db.Float, nullable=False)
status = db.Column(db.String(20), default=‘مفتوحة’)
created_at = db.Column(db.DateTime, default=datetime.utcnow)

def token_required(f):
@wraps(f)
def decorated(*args, **kwargs):
token = request.headers.get(‘Authorization’)
if not token:
return jsonify({‘رسالة’: ‘توكن مفقود’}), 401
try:
token = token.split(’ ’)[1]
data = jwt.decode(token, app.config[‘SECRET_KEY’], algorithms=[‘HS256’])
current_user = User.query.get(data[‘user_id’])
except:
return jsonify({‘رسالة’: ‘توكن غير صحيح’}), 401
return f(current_user, *args, **kwargs)
return decorated

@app.route(’/api/auth/register’, methods=[‘POST’])
def register():
data = request.json
if User.query.filter_by(username=data.get(‘username’)).first():
return jsonify({‘رسالة’: ‘اسم المستخدم موجود’}), 400
user = User(username=data.get(‘username’), email=data.get(‘email’))
user.set_password(data.get(‘password’))
db.session.add(user)
db.session.commit()
return jsonify({‘رسالة’: ‘تم التسجيل بنجاح’}), 201

@app.route(’/api/auth/login’, methods=[‘POST’])
def login():
data = request.json
user = User.query.filter_by(username=data.get(‘username’)).first()
if not user or not user.check_password(data.get(‘password’)):
return jsonify({‘رسالة’: ‘بيانات الدخول غير صحيحة’}), 401
token = jwt.encode({‘user_id’: user.id, ‘exp’: datetime.utcnow() + timedelta(days=30)}, app.config[‘SECRET_KEY’], algorithm=‘HS256’)
return jsonify({‘رسالة’: ‘تم تسجيل الدخول بنجاح’, ‘token’: token}), 200

@app.route(’/api/dashboard’, methods=[‘GET’])
@token_required
def dashboard(current_user):
trades = Trade.query.filter_by(user_id=current_user.id).all()
return jsonify({‘المستخدم’: current_user.username, ‘الرصيد’: current_user.balance}), 200

@app.route(’/api/trades’, methods=[‘GET’])
@token_required
def get_trades(current_user):
trades = Trade.query.filter_by(user_id=current_user.id).all()
return jsonify([{‘الرقم’: t.id, ‘العملة’: t.symbol} for t in trades]), 200

@app.route(’/’)
def index():
return jsonify({‘رسالة’: ‘نجد تعمل’}), 200

if **name** == ‘**main**’:
with app.app_context():
db.create_all()
port = int(os.environ.get(‘PORT’, 5000))
app.run(debug=False, host=‘0.0.0.0’, port=port)
