from flask import render_template, redirect, url_for
from app import app, db
from app.models import User
from datetime import datetime
from sqlalchemy import case

@app.route('/')
def index():
    users = User.query.order_by(
        User.afastado.asc(),  # Primeiro os não afastados
        case(
            (User.dataDispensa == None, 1),
            else_=0
        ).asc(),
        User.dataDispensa.asc()
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