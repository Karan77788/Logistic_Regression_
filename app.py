from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('logreg_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'age': int(request.form['age']),
            'job': request.form['job'],
            'marital': request.form['marital'],
            'balance': float(request.form['balance']),
            'duration': float(request.form['duration']),
        }
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        result = "Yes" if prediction == 1 else "No"
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
