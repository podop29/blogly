"""Seed file for testing"""


from models import User,Post, db
from app import app

db.drop_all()
db.create_all()


stevan = User(first_name='Stevan',last_name='Grubac',img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZDjUNOOX4fQTDX6ONMMElz9fp36XoVtXOCg&usqp=CAU')
ana = User(first_name='Ana',last_name='Grubac',img_url='https://i.ytimg.com/vi/U1590XqOYTY/maxresdefault.jpg')
jacoby = User(first_name='Jacoby',last_name='Cantolupo')


post1 = Post(title="Cheeze-Itz", content="ThEY R SOoo good mmmh", user_id=1)
post2 =  Post(title="luffy", content="hes so good", user_id=2)

db.session.add(stevan)
db.session.add(jacoby)
db.session.add(ana)


db.session.commit()
db.session.add(post1)
db.session.add(post2)


db.session.commit()


