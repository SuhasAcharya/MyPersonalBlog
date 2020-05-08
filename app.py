from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
db=SQLAlchemy(app)

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    review = db.Column(db.Text,nullable=False)
    
    rate = db.Column(db.Integer,nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.now().replace(microsecond=0))

    def __repr__(self):
        return 'USER ' + str(self.id)

@app.route('/',methods=['GET'])
def home():
    return render_template('about.html')


@app.route('/users',methods=['GET','POST'])
def users():
    if request.method == 'POST':
        name=request.form['name']
        review=request.form['review']
        rate=request.form['rate']
        new_user=Users(name=name,review=review,rate=rate)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/users')
    else:
        all_user = Users.query.order_by(Users.date_posted).all()
        return render_template('main.html',users=all_user)



@app.route('/users/new',methods=['POST','GET'])
def new():
    if request.method == 'POST':
        name=request.form['name']
        review=request.form['review']
        rate=request.form['rate']
        new_user=Users(name=name,review=review,rate=rate)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/users')
    else:

        return render_template('new.html')

@app.route('/users/delete/<int:id>')
def delete(id):
    user =Users.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')


@app.route('/users/edit/<int:id>' ,methods=['POST','GET'])
def edit(id):
    user=Users.query.get_or_404(id)
    if request.method=='POST':
        user.date_posted =datetime.now().replace(microsecond=0)
        user.name=request.form['name']
        user.review=request.form['review']
        user.rate=request.form['rate']
        db.session.commit()
        return redirect('/users')
    else:
        return render_template('edit.html',user=user)

@app.route('/home',methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug = True)




