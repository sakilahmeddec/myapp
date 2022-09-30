
from flask import Flask, render_template, request
import calendar
import datetime
import filecheck

app = Flask(__name__)
target = 2500
date = datetime.datetime.now()
date_month = date.month
total_date = calendar.monthrange(date.year, date_month)[1]
if total_date == date.day:
    remain_d = 1
else:
    remain_d = total_date - date.day

filecheck.main()


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
        file = open(f'{date.year}/{date_month}.txt', 'r')
        list_line = file.readlines()
        list_line[date.day - 1] = form_data['achive']
        file = open(f'{date.year}/{date_month}.txt', 'w')
        file.writelines(list_line)
        file.close()
        achiv_til = list_line[:date.day]
        a_t = sum(list(map(int, achiv_til)))
        l_f = open(f'{date.year}/{date_month - 1}.txt', 'r')
        list_last_m = l_f.readlines()
        last_month_t = list_last_m[date.day - 1]
        l_ach_till_d = list_last_m[:date.day]
        l_t_d = sum(list(map(int, l_ach_till_d)))

        return render_template('data.html', form_data=form_data, float=float, round=round, int=int, r_m=remain_d,
                               T=target, a_t_d=a_t,
                               l_m_t=last_month_t,
                               last_m_t_date=l_t_d)


if __name__ == "__main__":
    app.run()
