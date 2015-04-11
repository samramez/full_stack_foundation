__author__ = 'samramez'

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    # Mapper:
    # nullable = False is telling if there is no value for this, don't make the table.
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

class MenuItem(Base):
    __tablename__ = 'menu_item'

    # Mapper:
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

# Pointing to the database that we want to use
engine = create_engine('sqlite:///restaurantmenu.db')

# Goes into the database and add classes as new tables
Base.metadata.create_all(engine)
