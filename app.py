from flask import Flask, jsonify

app = Flask(**name**)

@app.route(’/’)
def hello():
return jsonify({“message”: “مرحبا بك في نجد”})

@app.route(’/api/test’)
def test():
return jsonify({“status”: “تطبيق نجد يعمل بنجاح”})

if **name** == ‘**main**’:
app.run(host=‘0.0.0.0’, port=5000, debug=False)
