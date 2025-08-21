from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Phone = db.Column(db.String(20))
    Incident = db.Column(db.String(50))
    Description = db.Column(db.Text)
    Location = db.Column(db.String(100))
    Date = db.Column(db.String(50))

class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.Text)
    bot_reply = db.Column(db.Text)
