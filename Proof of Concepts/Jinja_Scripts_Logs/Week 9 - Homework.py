#Eric Somogyi ID#

'''
1) 2.5 Points: Create a Python Flask app that reads a YAML config
from config.yaml, converts the format to JSON, and returns the JSON data
to the user (in the browser) whenever the /config_info route(path) is accessed.
'''


import yaml
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/config_info', methods=['GET'])
def display_config_info():
    with open('config.yaml', 'r') as f:
        data_yaml = yaml.safe_load(f)
    return jsonify(data_yaml)   

#after I run the app, I can access the config info at http://127.0.0.1:5000/config_info as a user typing it in the browser.

if __name__ == '__main__':
    app.run(debug=True)



#-------------------------------------------------------------------------

'''
2) 3.5 Points: Create a Python script that reads logs from the system.log
log file and uses a Jinja template to make an HTML page identical to the
the output shown in logs.html. The template should display a
dynamic timestamp from when the log file was generated. Your logic for 
processing the logs should be done in the Jinja template. (Log Parsing)
I won't take points off for spacing in your HTML code as long as it works.
Your script should output the html to a file called <yourlastname>-logs.html.

Include your .j2 template and html page in your homework submission.
'''

#filename of .j2 template: Eric_HW9_Jinja2template.j2
#filename of html page: somogyi-logs.html

import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime 

def generate_log_html(raw_log_file, html_output_file):
    with open(raw_log_file, 'r') as f:
        logs = f.readlines()

    env = Environment(loader = FileSystemLoader('.'))      
    env.globals['now'] = datetime.now
    template = env.get_template('Eric_HW9_Jinja2template.j2')
    Jinja_html = template.render(logs=logs)

    with open(html_output_file, 'w') as f:
        f.write(Jinja_html)

generate_log_html('system3.log', 'somogyi-logs.html')
