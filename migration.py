from flaskblock import db
from flaskblock.models import User, Post
from flaskblock.data_config import users, posts

db.drop_all()
db.create_all()

for user in users:
	new_user = User(**user)
	db.session.add(new_user)
	db.session.commit()

for post in posts:
	new_post = Post(**post)
	db.session.add(new_post)
	db.session.commit()
