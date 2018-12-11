from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship




engine = create_engine('sqlite:///calendar.db', echo=True)
base = declarative_base()

class Calendar(base):
    __tablename__ = "Calendar"

    id = Column(Integer, primary_key=True)
    event = Column(String)
    date = Column(Date)
    institution = relationship("Institution")

    def __init__(self, name):
        self.name = name

class Institution(base):
    __tablename__ = "institution"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    symbol = Column(String, nullable=True)



if __name__ == "__main__":
    base.metadata.create_all(engine)
    build_sample_data()
