import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_data_file(data):
    with open('database.txt', 'a') as database1:
        email = data['email']
        subject = data['subject']
        text = data['message']
        file = database1.write(f'email: {email}\nsubject: {subject}\nmessage: {text}\n')


def write_data_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        text = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, text])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data_file(data)
            write_data_csv(data)
            return redirect('./thankyou.html')
        except FileNotFoundError:
            return 'did not save to database'
    else:
        return 'something went wrong'
