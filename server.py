import os
from flask import Flask, render_template, send_from_directory, url_for , request, redirect
import csv 

app = Flask(__name__)

#Each route is wrapped into a function for the server to deploy.
@app.route("/") # < > route arguments that we can apply - <dtype: name> is the syntax
def index():
    return render_template('index.html')

@app.route("/<string:page_name>") 
def pager(page_name):
    return render_template(page_name)

# provide the small icon reprsenting the site
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/assets/'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

"""
#save the form inputs to a text file 
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["text"]
        file = database.write(f'\n{email},{subject},{message}')
"""
# Save data to CSV - in this case for the contact form for the portfolio site
def write_to_csv(data):
    with open('database.csv', mode='a',newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["text"]
        csv_writer = csv.writer(database, delimiter=',', quotechar=' ',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# keep the information being inputted into the contact form 
# the form exists on the contact.html page
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        print("try again")