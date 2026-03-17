#!/usr/bin/env python3

# نجد - منصة التداول الذكية

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import os
from datetime import datetime, timedelta

app = Flask(**name**)
app.config[‘SECRET_KEY’] = os.environ.get(‘SECRET_KEY’, ‘najd-trading-secret’)
app.config[‘SQLALCHEMY_DATABASE_URI’] = os.environ.get(‘DATABASE_URL’, ‘sqlite:///najd.db’)
app.config[‘SQLALCHEMY_TRACK_MODIFICATIONS’] = False

CORS(app)
db = SQLAlchemy(app)

# ============ DATABASE MODELS ============

class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
password = db.Column(db.String(200), nullable=False)
binance_api_key = db.Column(db.String(300))
binance_api_secret = db.Column(db.String(300))
balance = db.Column(db.Float, default=10000)
invested = db.Column(db.Float, default=0)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
trades = db.relationship(‘Trade’, backref=‘user’, lazy=True)
settings = db.relationship(‘UserSettings’, backref=‘user’, uselist=False)

```
def set_password(self, password):
    self.password = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password, password)
```

class Trade(db.Model):
id = db.Column(db.Integer, primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey(‘user.id’), nullable=False)
symbol = db.Column(db.String(20), nullable=False)
action = db.Column(db.String(10), nullable=False)
quantity = db.Column(db.Float, nullable=False)
price = db.Column(db.Float, nullable=False)
amount = db.Column(db.Float, nullable=False)
entry_price = db.Column(db.Float)
exit_price = db.Column(db.Float)
stop_loss = db.Column(db.Float)
take_profit = db.Column(db.Float)
status = db.Column(db.String(20), default=‘مفتوحة’)
profit_loss = db.Column(db.Float, default=0)
confidence = db.Column(db.Float)
created_at = db.Column(db.DateTime, default=datetime.utcnow)

class UserSettings(db.Model):
id = db.Column(db.Integer, primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey(‘user.id’), nullable=False)
max_position_size = db.Column(db.Float, default=100)
stop_loss_percent = db.Column(db.Float, default=3)
take_profit_percent = db.Column(db.Float, default=8)
auto_trading = db.Column(db.Boolean, default=True)
min_confidence = db.Column(db.Float, default=75)
created_at = db.Column(db.DateTime, default=datetime.utcnow)

class MarketAnalysis(db.Model):
id = db.Column(db.Integer, primary_key=True)
symbol = db.Column(db.String(20), nullable=False)
recommendation = db.Column(db.String(20))
confidence = db.Column(db.Float)
rsi = db.Column(db.Float)
macd = db.Column(db.Float)
price = db.Column(db.Float)
created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ============ AUTH DECORATOR ============

def token_required(f):
@wraps(f)
def decorated(*args, **kwargs):
token = request.headers.get(‘Authorization’)
if not token:
return jsonify({‘الرسالة’: ‘توكن مفقود’}), 401
try:
token = token.split(’ ’)[1]
data = jwt.decode(token, app.config[‘SECRET_KEY’], algorithms=[‘HS256’])
current_user = User.query.get(data[‘user_id’])
except:
return jsonify({‘الرسالة’: ‘توكن غير صحيح’}), 401
return f(current_user, *args, **kwargs)
return decorated

# ============ AUTH ROUTES ============

@app.route(’/api/auth/register’, methods=[‘POST’])
def register():
data = request.json
if User.query.filter_by(username=data.get(‘username’)).first():
return jsonify({‘الرسالة’: ‘اسم المستخدم موجود بالفعل’}), 400

```
user = User(username=data.get('username'), email=data.get('email'))
user.set_password(data.get('password'))
settings = UserSettings(user=user)

db.session.add(user)
db.session.add(settings)
db.session.commit()

return jsonify({'الرسالة': 'تم التسجيل بنجاح'}), 201
```

@app.route(’/api/auth/login’, methods=[‘POST’])
def login():
data = request.json
user = User.query.filter_by(username=data.get(‘username’)).first()

```
if not user or not user.check_password(data.get('password')):
    return jsonify({'الرسالة': 'بيانات الدخول غير صحيحة'}), 401

token = jwt.encode(
    {'user_id': user.id, 'exp': datetime.utcnow() + timedelta(days=30)},
    app.config['SECRET_KEY'],
    algorithm='HS256'
)

return jsonify({
    'الرسالة': 'تم تسجيل الدخول بنجاح',
    'token': token,
    'المستخدم': {
        'username': user.username,
        'email': user.email,
        'الرصيد': user.balance
    }
}), 200
```

# ============ DASHBOARD ROUTES ============

@app.route(’/api/dashboard’, methods=[‘GET’])
@token_required
def dashboard(current_user):
trades = Trade.query.filter_by(user_id=current_user.id).all()
total_profit = sum(t.profit_loss for t in trades if t.profit_loss)
open_trades = [t for t in trades if t.status == ‘مفتوحة’]

```
return jsonify({
    'المستخدم': current_user.username,
    'الرصيد': f"${current_user.balance:.2f}",
    'المستثمر': f"${current_user.invested:.2f}",
    'إجمالي_الربح': f"${total_profit:.2f}",
    'عدد_الصفقات_المفتوحة': len(open_trades),
    'عدد_الصفقات_المغلقة': len([t for t in trades if t.status == 'مغلقة'])
}), 200
```

# ============ TRADING ROUTES ============

@app.route(’/api/trades’, methods=[‘GET’])
@token_required
def get_trades(current_user):
trades = Trade.query.filter_by(user_id=current_user.id).all()
trades_data = []

```
for trade in trades:
    trades_data.append({
        'الرقم': trade.id,
        'العملة': trade.symbol,
        'الإجراء': 'شراء' if trade.action == 'BUY' else 'بيع',
        'السعر': f"${trade.price:.2f}",
        'المبلغ': f"${trade.amount:.2f}",
        'الحالة': trade.status,
        'التاريخ': trade.created_at.strftime('%Y-%m-%d %H:%M')
    })

return jsonify(trades_data), 200
```

@app.route(’/api/trade/execute’, methods=[‘POST’])
@token_required
def execute_trade(current_user):
data = request.json

```
trade = Trade(
    user_id=current_user.id,
    symbol=data.get('symbol'),
    action=data.get('action'),
    quantity=data.get('quantity'),
    price=data.get('price'),
    amount=data.get('amount'),
    entry_price=data.get('entry_price'),
    stop_loss=data.get('stop_loss'),
    take_profit=data.get('take_profit'),
    confidence=data.get('confidence', 0)
)

if data.get('action') == 'BUY':
    current_user.balance -= data.get('amount', 0)
    current_user.invested += data.get('amount', 0)
elif data.get('action') == 'SELL':
    current_user.balance += data.get('amount', 0)
    current_user.invested = max(0, current_user.invested - data.get('amount', 0))

db.session.add(trade)
db.session.commit()

return jsonify({
    'الرسالة': '✅ تم تنفيذ الصفقة',
    'رقم_الصفقة': trade.id,
    'العملة': data.get('symbol'),
    'الإجراء': 'شراء' if data.get('action') == 'BUY' else 'بيع',
    'المبلغ': f"${data.get('amount'):.2f}",
    'الرصيد_الجديد': f"${current_user.balance:.2f}"
}), 201
```

# ============ SETTINGS ROUTES ============

@app.route(’/api/settings’, methods=[‘GET’, ‘POST’])
@token_required
def settings(current_user):
if request.method == ‘GET’:
settings_obj = current_user.settings
return jsonify({
‘حد_الصفقة_الأقصى’: settings_obj.max_position_size,
‘وقف_الخسارة’: f”{settings_obj.stop_loss_percent}%”,
‘جني_الأرباح’: f”{settings_obj.take_profit_percent}%”,
‘التداول_التلقائي’: settings_obj.auto_trading
}), 200

```
data = request.json
settings_obj = current_user.settings
settings_obj.stop_loss_percent = data.get('stop_loss_percent', settings_obj.stop_loss_percent)
settings_obj.take_profit_percent = data.get('take_profit_percent', settings_obj.take_profit_percent)
settings_obj.auto_trading = data.get('auto_trading', settings_obj.auto_trading)

db.session.commit()
return jsonify({'الرسالة': '✅ تم تحديث الإعدادات'}), 200
```

# ============ BINANCE SETUP ============

@app.route(’/api/setup/binance’, methods=[‘POST’, ‘GET’])
@token_required
def setup_binance(current_user):
if request.method == ‘GET’:
return jsonify({
‘مفتاح_API’: ‘✅ محفوظ’ if current_user.binance_api_key else ‘❌ غير موجود’,
‘مفتاح_السر’: ‘✅ محفوظ’ if current_user.binance_api_secret else ‘❌ غير موجود’
}), 200

```
data = request.json
current_user.binance_api_key = data.get('api_key')
current_user.binance_api_secret = data.get('api_secret')
current_user.settings.auto_trading = True

db.session.commit()
return jsonify({'الرسالة': '✅ تم حفظ مفاتيح Binance بنجاح'}), 200
```

# ============ MAIN ROUTES ============

@app.route(’/’)
def index():
return jsonify({‘الرسالة’: ‘✅ نجد - منصة التداول الذكية تعمل بنجاح’}), 200

@app.errorhandler(404)
def not_found(error):
return index()

if **name** == ‘**main**’:
with app.app_context():
db.create_all()

```
port = int(os.environ.get('PORT', 5000))
app.run(debug=False, host='0.0.0.0', port=port)
```
