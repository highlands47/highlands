from flask import Flask, render_template, url_for

app = Flask(__name__)


courses = [
    {

        'topic': 'Diploma in Business Administration',
        'duration': '6 Months',
        'price': '$175 per month',
        'course_date': 'January 15, 2019'
    },
    {
        'topic': 'Finance for Non-Finance Managers',
        'duration': '2 Months',
        'price': '$70 per month',
        'course_date': 'January 15, 2019'
    },
    {
        'topic': 'Networking',
        'duration': '3 Months',
        'price': '$176 per month',
        'course_date': 'January 16, 2019'
    }
]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', courses=courses)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/log_in')
def log_in():
    return render_template('log_in.html', title='Log In')

@app.route('/register')
def register():
    return render_template('register.html', title='register')

if __name__ == '__main__':
    app.run(debug=True)
