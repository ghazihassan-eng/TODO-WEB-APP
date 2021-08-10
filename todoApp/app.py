from enum import unique
from flask import Flask , render_template , request
from datetime import date, datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/todo'
db = SQLAlchemy(app)

class list(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.String(200),unique=False)
    date = db.Column(db.String(15))

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    List=list.query.all()
    if request.method=='POST':
        title = request.form.get('title')
        description = request.form.get('desc')

        entry=list(title=title,description=description,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    List=list.query.all()
        

    return render_template('index.html',li=List)

@app.route('/delete/<string:SNo>',methods=['GET','POST'])
def delete(SNo):
    li=list.query.filter_by(SNo=SNo).first()
    db.session.delete(li)
    db.session.commit()

    List=list.query.all()
    return render_template('index.html',li=List)

if __name__ == "__main__":
    app.run(debug=True)