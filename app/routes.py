from flask import render_template, flash, redirect, url_for, request
from app import db
from app.models import Thought
from flask import Blueprint
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    thoughts = Thought.query.order_by(Thought.timestamp.desc()).all()
    return render_template('index.html', thoughts=thoughts)

@bp.route('/add', methods=['GET', 'POST'])
def add_thought():
    if request.method == 'POST':
        content = request.form['content']
        mood = request.form.get('mood', '')
        category = request.form.get('category', '')
        
        if content:
            thought = Thought(content=content, mood=mood, category=category)
            db.session.add(thought)
            db.session.commit()
            flash('Your thought has been recorded!')
            return redirect(url_for('main.index'))
    
    return render_template('add_thought.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_thought(id):
    thought = Thought.query.get_or_404(id)
    
    if request.method == 'POST':
        thought.content = request.form['content']
        thought.mood = request.form.get('mood', '')
        thought.category = request.form.get('category', '')
        db.session.commit()
        flash('Your thought has been updated!')
        return redirect(url_for('main.index'))
    
    return render_template('edit_thought.html', thought=thought)

@bp.route('/delete/<int:id>')
def delete_thought(id):
    thought = Thought.query.get_or_404(id)
    db.session.delete(thought)
    db.session.commit()
    flash('Your thought has been deleted!')
    return redirect(url_for('main.index'))

@bp.route('/random')
def random_thought():
    thought = Thought.query.order_by(db.func.random()).first()
    return render_template('random_thought.html', thought=thought)