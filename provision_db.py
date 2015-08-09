# -*- coding: utf-8 -*-
__author__ = 'seb'


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


user1 = User(name="Luki", email="test@test.com")

session.add(user1)
session.commit()

items = []

items.append(Category(user_id=1, description="Theresa Cat 1"))
items.append(Category(user_id=1, description="Theresa Cat 2"))
items.append(Category(user_id=2, description="Seb Cat 1"))

items.append(Item(user_id=1, category_id=1, title="Ein Titel",
                  description="Eine Beschreibung"))
for item in items:
    session.add(item)
    session.commit()


print("done")