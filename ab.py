from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_structure.php?server=1&db=ppp'
db = SQLAlchemy(app)

class pppp(db.Model):
    '''
        	firstname, lastname, email, country, address,information,subject
        '''
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(90), nullable=False)
    country = db.Column(db.String(120), nullable=False)
    address= db.Column(db.String(100), nullable=False)
    information= db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)





@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/ppp", methods = ['GET', 'POST'])
def ppp():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        country = request.form.get('country')
        address = request.form.get('address')
        information = request.form.get('information')
        subject = request.form.get('subject')
        entry = pppp(firstname=firstname, lastname=lastname, email=email, country=country, address=address,information=information,subject=subject)
        db.session.add(entry)
        db.session.commit()
    return render_template('ppp.html')

@app.route('/axx')
def axx():
    return render_template('axx.html')

@app.route('/dx')
def dx():
    return render_template('dx.html')
if __name__ == '__main__':
    app.run(debug=True)
