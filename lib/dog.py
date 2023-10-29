from models import Dog
# from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///dogs.db')
# base = declarative_base()

def create_table(base,engine):
    # engine()
    base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    return session.query(Dog).all()
    

def find_by_name(session, name):
    name_query = session.query(Dog).filter(Dog.name == name)
    # for dog in name_query:
    return name_query.first()

def find_by_id(session, id):
    name_query = session.query(Dog).filter(Dog.id == id)
    # for dog in name_query:
    return name_query.first()

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name.like(name), Dog.breed == breed)
    for name in dog:
        return name
    

def update_breed(session, dog, breed):
    name = dog.name
    the_dog = find_by_name(session,name)
    the_dog.breed = breed
    session.add(the_dog)
    session.commit()