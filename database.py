from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://posttest:1@localhost/appdb"
engine = create_engine(DATABASE_URL, echo=True)  # database log echo = True

Base = declarative_base()
Session = sessionmaker(bind=engine)
