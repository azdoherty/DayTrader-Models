from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///calendar.db', echo=True)
base = declarative_base()


class Calendar(base):
    __tablename__ = "Calendar"
    id = Column(Integer, primary_key=True)
    event = Column(String)
    date = Column(Date)
    institution = relationship("Institution")


class Institution(base):
    __tablename__ = "institution"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    symbol = Column(String, nullable=True)



if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = Institution()
    session.add(ins)
    q = session.query(ins).all()

    for item in q:
        print(f"{q.id} {q.name} {q.symbol}")




