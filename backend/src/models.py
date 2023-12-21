from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

cliente_event = db.Table('cliente_event',
    db.Column('cliente_id', db.Integer, db.ForeignKey('client.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)
class Cliente(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telephone = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    events = db.relationship('Evento', secondary=cliente_event, backref=db.backref('clients', lazy='dynamic'))

class Evento(db.Model):
    __tablename__='event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_event = db.Column(db.String(50), nullable=False)
    local = db.Column(db.String(50), nullable=False)
    company = db.Column(db.String(50), nullable=False)
    genere = db.Column(db.String(50), nullable=False)
    is_free = db.Column(db.Boolean, default=True)
    