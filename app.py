from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    
    def __init__(self,name,email,message):
        self.name = name
        self.email = email
        self.message = message



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        contact_form = Contact(name=name, email=email, message=message)
        db.session.add(contact_form)
        db.session.commit()
        if contact_form.id:
           return render_template(('thank_you.html'))
        else:
            return "Error: Failed to add the record"

        
    return render_template('contact.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')    

@app.route('/MyWork')
def MyWork():
    return render_template('MyWork.html')  

@app.route('/ProductDesign')
def ProductDesign():
    return render_template('ProductDesign.html')

@app.route('/AppDesign')
def AppDesign():
    return render_template('AppDesign.html')    


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':

    with app.app_context():
         db.create_all()  # create the table before running the app
    app.run(debug=True)