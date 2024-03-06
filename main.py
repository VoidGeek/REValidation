import re
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='demo')

def validate_password(password):
    """
    Function to validate the password using regular expressions.
    Returns True if the password meets the criteria, False otherwise.
    """
    # Define the regular expression pattern for password validation
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Check if the password matches the pattern
    password_valid = bool(re.match(password_pattern, password))
    return password_valid

def validate_email(email):
    """
    Function to validate the email address using regular expressions.
    Returns True if the email address is valid, False otherwise.
    """
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_pattern, email))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate_password', methods=['POST'])
def validate_password_endpoint():
    password = request.form['password']
    password_valid = validate_password(password)
    return render_template('result.html', password_valid=password_valid)

@app.route('/validate_email', methods=['POST'])
def validate_email_endpoint():
    email = request.form['email']
    email_valid = validate_email(email)
    return render_template('result.html', email_valid=email_valid)

if __name__ == '__main__':
    app.run(debug=True)
