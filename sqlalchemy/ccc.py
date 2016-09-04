from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(VARCHAR(40))
    email = Column(VARCHAR(50))

class Address(Base):
    __tablename__ ='address'

    id = Column(Integer,primary_key=True)
    addname = Column(VARCHAR(50))
    user_id = Column(Integer,ForeignKey(Users.id))

def query(session):
    #que_users = session.query(Users)
    que_addr = session.query(Address)
    #过滤
    '''res1 = que_users.filter('id>:id').params(id=7).all()
    res2 = que_users.filter_by(name='bob').all()
    res3 = que_users.filter(Users.name.like('%y%')).all()
    res4 = session.query(Users,Address).filter(Users.id==Address.user_id).all()'''
    res5 = session.query(Users).join(Address).all()
    #res6 = session.query(Address).filter(Address.id==1).one()
    print(res5[0].id)

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:123@localhost:3306/test', echo=True)

    session = create_session(bind=engine)
    #session = sessionmaker(bind=engine)
    query(session)
