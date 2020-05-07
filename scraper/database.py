import sqlalchemy, os, uuid
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import BYTEA, REAL
from sqlalchemy.orm import sessionmaker

PATH_TO_DB = os.path.join(os.getcwd(), 'app', 'database', 'newsfeed.db')

engine = create_engine("postgresql://postgres:12345@localhost:5432/newsfeed",echo=True)
Session = sessionmaker(bind=engine)
# metadata = MetaData()
Base = declarative_base()

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True, nullable=False)
    country = Column(String, nullable=False)
    title = Column(BYTEA, unique=True, nullable=False)
    body = Column(BYTEA, nullable=False)
    source = Column(String, nullable=False)
    lastupdated = Column(String, nullable=False)
    category = Column(String)
    accuracy = Column(REAL)

    def __repr__(self):
        return f"<News(title={self.title}, source={self.source}, lastupdated={self.lastupdated})>"

#news = Table('news', metadata, autoload=True, autoload_with=engine)


def addToNews(country: str, title: str, body: str, source: str, lastupdated: str):
    session = Session()
    try:
        news = News(public_id=str(uuid.uuid4()), country=country, title=title, body=body, source=source, lastupdated=lastupdated)
        session.add(news)
        session.commit()
    except sqlalchemy.exc.IntegrityError:
        return