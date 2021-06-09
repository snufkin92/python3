import sqlalchemy.ext.declarative
import sqlalchemy.orm

# テーブル作成の為、メモリで試す(echo=Trueで実行したクエリーが出力される）
engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


# テーブルを作成
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

person_1 = Person(name='Mike')
person_2 = Person(name='Nancy')
person_3 = Person(name='Nancy')
session.add(person_1)
session.add(person_2)
session.add(person_3)
session.commit()

# 戻り値は list
persons = session.query(Person).all()
print(type(persons))

for person in persons:
    print(person.id, person.name)

print("### filter_by is like where statement")

Nancys = session.query(Person).filter_by(name='Nancy').all()

for person in Nancys:              
    print(person.id, person.name)
