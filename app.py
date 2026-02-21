from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

def get_user_todo_model(username):
    class Todo(db.Model):
        __tablename__ = f'todo_{username}'
        __table_args__ = {'extend_existing': True}

        sl_no=db.Column(db.Integer, primary_key=True)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        title=db.Column(db.String(200), nullable=True)
        todo=db.Column(db.String(600), nullable=False)
        important=db.Column(db.Boolean, default=False)

        def __repr__(self)-> str:
            return f"{self.sl_no} - {self.title} - {self.todo}"
    return Todo
    

@app.route('/')
def hello_World():
    return render_template('home.html')

@app.route('/index/<username>', methods=['GET','POST'])
def index_page(username):
    Todo = get_user_todo_model(username)
    db.create_all()
    if request.method=='POST':
        title=request.form['title']
        todo=request.form['todo']
        todo_list= Todo(todo=todo,title=title)
        db.session.add(todo_list)
        db.session.commit()
    allTodo=Todo.query.all()
    return render_template('index.html',allTodo=allTodo,username=username)

@app.route('/search/<username>', methods=['GET'])
def search(username):
    Todo = get_user_todo_model(username)
    db.create_all()
    search_query = request.args.get('search')
    
    # Search Logic: Filters by title or the todo content
    if search_query:
        allTodo = Todo.query.filter(
            (Todo.title.contains(search_query)) | 
            (Todo.todo.contains(search_query))
        ).all()
    else:
        allTodo = Todo.query.all()
        
    return render_template('search.html', allTodo=allTodo, search_query=search_query,username=username)

@app.route('/add/<username>', methods=['GET','POST'])
def add(username):
    Todo = get_user_todo_model(username)
    db.create_all()
    if request.method=='POST':
        is_completed = request.form.get('important') == 'on'
        title=request.form['title']
        todo=request.form['todo']
        todo_list= Todo(todo=todo,title=title,important=is_completed)
        db.session.add(todo_list)
        db.session.commit()
        return redirect(url_for('index_page',username=username))
    allTodo=Todo.query.all()
    return render_template('add.html',allTodo=allTodo,username=username)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/delete/<username>/<int:sl_no>')
def delete(username,sl_no):
    Todo = get_user_todo_model(username)

    todo=Todo.query.filter_by(sl_no=sl_no).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index_page',username=username))

@app.route('/update/<username>/<int:sl_no>',methods=['GET','POST'])
def update(username,sl_no):
    Todo = get_user_todo_model(username)
    db.create_all()
    if request.method=='POST':
        up_title=request.form['up_title']
        update=request.form['update']
        todo= Todo.query.filter_by(sl_no=sl_no).first()
        todo.title=up_title
        todo.todo=update
        todo.important = request.form.get('important') == 'on'
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index_page',username=username))
    
    todo=Todo.query.filter_by(sl_no=sl_no).first()
    return render_template('update.html',Todo=todo,username=username)

if __name__ == '__main__':
    app.run(debug=True)
