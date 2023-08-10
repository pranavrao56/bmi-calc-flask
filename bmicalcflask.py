# BMI Calculator using Flask
from flask import Flask, render_template, request

app = Flask(__name__)


def message(bmi):
    if bmi < 18.5:
        msg = "You are underweight"
    elif 18.5 <= bmi < 25:
        msg = "You are healthy"
    elif 25 <= bmi < 30:
        msg = "You are overweight"
    else:
        msg = "You are obese"
    return msg


@app.route("/", methods=['POST', 'GET'])
def calc_bmi():
    bmi = ''
    msg = ''
    if request.method == 'POST' and 'Weight' in request.form and 'Height' in request.form:
        h = float(request.form.get('Height'))
        w = float(request.form.get('Weight'))
        bmi = round(w / (h * h), 2)
        msg = message(bmi)
    return render_template('index.html', bmi=bmi, msg=msg)


if __name__ == '__main__':
    app.run()
