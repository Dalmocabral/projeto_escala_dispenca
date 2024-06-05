from flask import render_template, redirect, url_for
from app import app, db
from app.models import User
from datetime import datetime

@app.route('/')
def index():
    users = User.query.order_by(
        User.afastado.asc(),  # Primeiro os não afastados
        User.dataDispensa.asc().nullsfirst()  # Depois os que não têm data de dispensa (nullsfirst faz com que nulls venham primeiro)
    ).all()
    return render_template('index.html', users=users)


@app.route('/dispensa/<int:user_id>', methods=['POST'])
def dispensa(user_id):
    user = User.query.get_or_404(user_id)
    user.dataDispensa = datetime.utcnow()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/afastamento/<int:user_id>', methods=['POST'])
def afastamento(user_id):
    user = User.query.get_or_404(user_id)
    user.afastado = not user.afastado  # Alterna o estado de afastamento
    db.session.commit()
    return redirect(url_for('index'))