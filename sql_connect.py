#Session is a way to connect to an engine, it's the doorway
#You can create a new object by defining it in term of tablename(column1, column2 etc.)
#When you create this object, it's just an instance.
#If you don't create the primary key value (id) it will recognise that it's a new entry automatically
#session.add() attaches the object to the current session, and is now ready to be sent to the DB
#session.commit() creates it in the database
##Existing database:
# from sqlalchemy import MetaData, Table
#metadata = MetaData()
#information = Table('Information', metadata, autoload = true, autoload_with=engine)
#print(repr(information))
#


import os
PWD = os.path.abspath(os.curdir)

from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table
from sqlalchemy import Column, Integer, Numeric, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from yaml import safe_load, load, dump

#engine = create_engine('sqlite:///EVE_market.db', echo = True)
engine = create_engine('sqlite:///EVE_analysis.sqlite', echo = True)

##Session:
from sqlalchemy.orm import sessionmaker

##Create metadata
Base = declarative_base()
metadata = MetaData()

class Information(Base):
    __tablename__ =  'listings'
    id = Column(Integer, primary_key=True)
    duration=Column(Integer())
    is_buy_order = Column(Boolean())
    issued = Column(Integer())
    location_id = Column(Integer())
    order_id = Column(Integer())
    price = Column(Numeric(100, 2))
    range = Column(String(10))
    system_id = Column(Integer())
    type_id = Column(Integer())
    volume = Column(Integer())
    name = Column(String(60), index=True)
    quantity = Column(Integer())
    station = Column(String(50), index=True)
    region_id = Column(Integer())


##This section works.
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
#order1 = Information(order_id = 100, type_id = 34, name = "Tritanium", price = 3.45, quantity = 1000, station = "Jita", region_id = 10000002)
#session.add(order1)
#session.commit()

#session.close()

## REFLECT DATABASE STRUCTURE INTO CODE
engine = create_engine('sqlite:///EVE_analysis.sqlite', echo = True)
Session.configure(bind=engine)
meta = MetaData()
meta.reflect(bind=engine)
MarketGroups = meta.tables['invMarketGroups']



#Search marketgroups based upon text.
#attempting to do the following results in error code: AttributeError: 'Table' object has no attribute 'marketGroupName'
Session.configure(bind=engine)

#Still errors with Table object having no attribute called marketGroupName
#This just searches the names. DON'T ACTUALLY DO THIS.

#que = session.query(MarketGroups).filter(MarketGroups.c.marketGroupName == 'Implants')
que = query.filter(or_MarketGroups.marketGroupName == 'Implants')

#, "Ships", "Ship Equipment", "Hull & Armor"

#need to select MarketGroupID where marketGroupName meets some condition!




que = session.query(MarketGroups.c.marketGroupName)

#Suddenly works when I added the .c. into it

#Step 1. Find the marketGroupID where marketGroupName == 'Implants', 'Ships', 'Ship Equipment', 'Hull & Armor',
#JOIN CODE. JOIN CLAUSE COMBINES ROWS OF TWO OR MORE TABLES BASED UPON A RELATED COLUMN BETWEEN THEM.
#join based upon marketGroupID.
#





## Final result of all these queries needs to be all the type IDs as a vector/list, in which to go through for our ESI endpoints.





##Commit Changes to Database
session = Session()
session.add(Information())
session.commit

info_marketids.columns

##Reflection
#info = Table('listings', metadata, autoload =True, autoload_with = engine)


##Query the database to find type_ids associated with group IDs.
#Use invMarketGroups table, then find marketGroupID based upon

#info = Table('invMarketGroups', metadata, autoLoad = True, autoload_with = engine)




