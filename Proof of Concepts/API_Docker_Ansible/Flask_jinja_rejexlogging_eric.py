#Eric Somogyi#


# Import python modules
from flask import Flask, render_template, request, redirect, url_for
import re, os, logging


# Instantiate Flask app and setup logging
app = Flask(__name__)
log_dir = os.path.join(os.path.dirname(__file__), 'web_log.log')
logging.basicConfig(
    level=logging.DEBUG, 
    filename=log_dir,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

# Add Flask route that targets the root directory
@app.route('/')
def index():

    # Define the fields and departments
    fields = {
        'first_name': {
            'name': 'firstname',
            'description': 'First Name:',
            'placeholder': 'Enter your first name'
        },
        'last_name': {
            'name': 'lastname',
            'description': 'Last Name:',
            'placeholder': 'Enter your last name'
        },
        'phone': {
            'name': 'phone',
            'description': 'Phone Number:',
            'placeholder': 'Enter your phone number'
        },
        'email': {
            'name': 'email',
            'description': 'Email Address:',
            'placeholder': 'Enter your email address'
        },
    }

    departments = [
        {'id': 'HR', 'name': 'Human Resources'},
        {'id': 'IT', 'name': 'Information Technology'},
        {'id': 'Finance', 'name': 'Finance'},
        {'id': 'Marketing', 'name': 'Marketing'},
        {'id': 'Sales', 'name': 'Sales'}
    ]


    # Logging debug message that states the template is being rendered
    logging.debug("Rendering template...")
    # Display the rendered Jinja template
    return render_template('register.j2', fields=fields, departments=departments)   



# Add Flask route that lets user post form data
@app.route('/register', methods=['POST'])
def register():

    # Get form data
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    phone = request.form['phone']
    email = request.form['email']
    department = request.form['department']

    # Logging debug message that displays the collected form data
    logging.debug(f"Form data | First Name: {firstname}, | Last Name: {lastname}, | Phone: {phone}, | Email: {email}, | Department: {department}")

    # Define email regex
    email_regex = r'[a-z]+@[a-z]+\.[a-z]+'

    # Validate Email. If validation fails, call the error function and include an error message.
    if not re.match(email_regex, email):
        logging.error(f"Email Regex did not match. Email given: {email}")
        return redirect(url_for('error', error_message="Error Invalid email format. Please enter a valid email (e.g., user@domain.com)."))

    # Define phone regex
    phone_regex = r'^\d{3}-\d{3}-\d{4}$|^\d{10}$'

    # Validate Phone. If validation fails, call the error function and include an error message. 
    if not re.match(phone_regex, phone):
        logging.error(f"Phone Regex did not match. Phone given: {phone}")
        return redirect(url_for('error', error_message="Error Invalid phone number. Please enter a valid phone number."))


    # Logging info message that states the user is registered successfully.
    logging.info(f"User registered! | First Name: {firstname}, | Last Name: {lastname}, | Phone: {phone}, | Email: {email}, | Department: {department}")
    return redirect(url_for('index'))
    


#Add a Flask route that displays an error if incorrect format is submitted
@app.route('/error')
def error():

    # Get error message from URL parameter
    error_message = request.args.get('error_message')
    logging.debug(f"Error message: {error_message}")
    # Logging info message stating the error template has been rendered
    logging.debug("Error template rendered...")
    # Render error HTML code that displays error message from parameter
    return render_template('error.j2', error_message=error_message)

#run the Flask app and debug info
if __name__ == '__main__':
    # Run webserver
    logging.debug("Starting webserver.")
    if app.debug:
        logging.info("Debugger is active!!!!!!!!!!!!")
    app.run(host='0.0.0.0', port=5000, debug=True)
    logging.debug("The weberver is running.")






















#### original code##### FINAL - Part 2 #####
##### CSEC-380/480 - Kurt Wickboldt ####
#Eric Somogyi - esomogyi@depaul.edu - #2180405

# '''
# 2) 10 Points: Flask/Jinja/Regex/Logging. See PDF for Instructions.
# '''

# from flask import Flask, render_template, request, redirect, url_for
# import re
# import logging


# # Instantiate Flask app and setup logging

# # Add Flask route that targets the root directory
# def index():
#     fields = {
#         'first_name': {
#             'name': 'firstname',
#             'description': 'First Name:',
#             'placeholder': 'Enter your first name'
#         },
#         'last_name': {
#             'name': 'lastname',
#             'description': 'Last Name:',
#             'placeholder': 'Enter your last name'
#         },
#         'phone': {
#             'name': 'phone',
#             'description': 'Phone Number:',
#             'placeholder': 'Enter your phone number'
#         },
#         'email': {
#             'name': 'email',
#             'description': 'Email Address:',
#             'placeholder': 'Enter your email address'
#         },
#     }

#     departments = [
#         {'id': 'HR', 'name': 'Human Resources'},
#         {'id': 'IT', 'name': 'Information Technology'},
#         {'id': 'Finance', 'name': 'Finance'},
#         {'id': 'Marketing', 'name': 'Marketing'},
#         {'id': 'Sales', 'name': 'Sales'}
#     ]

#     # Logging debug message that states the template is being rendered

#     # Render Jinja template


# # Add Flask route that lets user post form data
# def register():
#     # Get form data
#     firstname = 
#     lastname = 
#     phone = 
#     email = 
#     department = 

    # Logging debug message that displays the collected form data
    

#     # Define email regex
#     email_regex = 

#     # Validate Email. If validation fails, call the error function and include an error message.
#     # Logging error message that states the incorrect email.

#     # Define phone regex
#     phone_regex = 

#     # Validate Phone. If validation fails, call the error function and include an error message. 
#     # Logging error message that states the incorrect phone number.


#     # If all inputs are valid, redirect to root/index
#     # Logging info message that states the user is registered successfully. (This is instead of performing a registration action)


# # Add a Flask route that displays an error if incorrect format is submitted
# def error():
#     # Get error message from URL parameter
#     # Logging info message stating the error template has been rendered
#     # Render error HTML code that displays error message from parameter

# if __name__ == '__main__':
#     # Run webserver
#     # Logging info message that states the webserver is running    