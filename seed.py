"""Seed file for testing"""


from models import User, db
from app import app

db.drop_all()
db.create_all()


stevan = User(first_name='Stevan',last_name='Grubac',img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZDjUNOOX4fQTDX6ONMMElz9fp36XoVtXOCg&usqp=CAU')
ana = User(first_name='Ana',last_name='Grubac',img_url='https://i.ytimg.com/vi/U1590XqOYTY/maxresdefault.jpg')
jacoby = User(first_name='Jacoby',last_name='Cantolupo')

db.session.add(stevan)
db.session.add(jacoby)
db.session.add(ana)

db.session.commit()

