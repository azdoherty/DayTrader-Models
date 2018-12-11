from sqlalchemy import create_engine, ForeignKey, Table, MetaData, Sequence
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///calendar.db', echo=True)
base = declarative_base()
metadata = MetaData()

Institutions = Table('Institutions', metadata,
   Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
   Column('name', String(50)),
   Column('symbol', String(50)),
)
metadata.create_all(engine)

companySymbols = {"Apple": "AAPL",
                  "Micron": "MU",
                  "J.P. Morgan Chase": "JPM",
                  "Federal Reserve": None
                  }

entries = []
for key, value in companySymbols.items():
    entries.append({"name}": key, "symbol": value})
print(entries)
conn = engine.connect()
ins = Institutions.insert()
conn.execute(ins, entries)


