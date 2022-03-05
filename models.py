from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    __tablename__ = 'User'

    def __repr__(self):
      return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name}"


    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    
    first_name = db.Column(db.String(20),
                            nullable=False)
    last_name = db.Column(db.String(20),
                            nullable=False)
    img_url = db.Column(db.String(), nullable = False, default="https://www.kindpng.com/picc/m/404-4042814_facebook-no-profile-png-download-default-headshot-transparent.png")

class Post(db.Model):
  __tablename__='post'

  id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

  title = db.Column(db.String(50),
                            nullable=False)

  content = db.Column(db.String(),
                            nullable=False)
  created_at =  db.Column(db.DateTime, default=datetime.datetime.utcnow)
  
  user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

