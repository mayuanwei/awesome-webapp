from sqlalchemy import *
from sqlalchemy.orm import *

def insert_table(table):
    ins = users_table.insert()
    ins.execute(name='bob',email='bob123@163.com')
    ins.execute({'name':'yujie','email':'jessica111@126.com'},{'name':'myw','email':'mayuanwei@gmail.com.cn'})
    '''ins_address = address_table.insert()
    ins_address.execute(addname='黄石路1号'.encode('utf-8'),user_id=8)'''

def select_table(table):
    sel = users_table.select(and_(users_table.c.id>1,users_table.c.id<3))
    print(sel.execute().fetchall())

def delete_table(table):
    dele = users_table.delete(users_table.c.name=='myw')
    dele.execute()

def update_table(table):
    upe = users_table.update(users_table.c.name=='bob')
    upe.execute(email='bobabc@126.com')

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:123@localhost:3306/test', echo=True)
    metadata = MetaData(bind=engine)

    '''users_table = Table('users',metadata,
                        Column('id',Integer,primary_key=True),
                        Column('name',String(30)),
                        Column('email',String(100))
                        )
    users_table.create()'''

    users_table = Table('users', metadata, autoload=True)
    address_table = Table('address',metadata,autoload=True)
    insert_table(users_table)
    #delete_table(users_table)
    #update_table(users_table)
