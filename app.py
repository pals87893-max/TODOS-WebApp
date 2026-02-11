from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

class Todo(db.Model):
    sl_no=db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    title=db.Column(db.String(200), nullable=True)
    todo=db.Column(db.String(600), nullable=False)

    def __repr__(self)-> str:
        return f"{self.sl_no} - {self.title} - {self.todo}"
    

@app.route('/')
def hello_World():
    return render_template('home.html')

@app.route('/index', methods=['GET','POST'])
def index_page():
    if request.method=='POST':
        title=request.form['title']
        todo=request.form['todo']
        todo_list= Todo(todo=todo,title=title)
        db.session.add(todo_list)
        db.session.commit()
    allTodo=Todo.query.all()
    return render_template('index.html',allTodo=allTodo)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method=='POST':
        title=request.form['title']
        todo=request.form['todo']
        todo_list= Todo(todo=todo,title=title)
        db.session.add(todo_list)
        db.session.commit()
        return redirect('/index')
    allTodo=Todo.query.all()
    return render_template('add.html',allTodo=allTodo)

@app.route('/delete/<int:sl_no>')
def delete(sl_no):
    todo=Todo.query.filter_by(sl_no=sl_no).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/index')

@app.route('/update/<int:sl_no>',methods=['GET','POST'])
def update(sl_no):
    if request.method=='POST':
        up_title=request.form['up_title']
        update=request.form['update']
        todo= Todo.query.filter_by(sl_no=sl_no).first()
        todo.title=up_title
        todo.todo=update
        db.session.add(todo)
        db.session.commit()
        return redirect('/index')
    
    todo=Todo.query.filter_by(sl_no=sl_no).first()
    return render_template('update.html',Todo=todo)

if __name__ == '__main__':
    app.run(debug=True)
