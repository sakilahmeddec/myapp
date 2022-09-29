from flask import Flask, render_template, request
import calendar
import datetime

app = Flask(__name__)
target = 2500
date = datetime.datetime.now()
date_month = date.month
total_date = calendar.monthrange(date.year, date_month)[1]
if total_date == date.day:
    remain_d = 1
else:
    remain_d = total_date - date.day



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/bank')
def bank():
    return render_template("bank.html")


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        # print(fff)
        # print(f"20 Fils x {form_data['tweF']}")
        return render_template('data.html', form_data=form_data, float=float, round=round, int=int, r_m=remain_d,
                               T=target)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)