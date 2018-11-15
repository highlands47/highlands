from flask import Flask, render_template, url_for, flash, redirect
from input_forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']= 'b34f6179271885500928d2f8442f57a5'  #Protects form from attacks

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
    form = LoginForm()  #Creates an instance of the class LoginForm imported from input_forms.py
    return render_template('log_in.html', title='Log In', form=form)  # form=form gives us access to the form=LoginForm() instance

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.first_name.data}!', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
