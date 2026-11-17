from sqlalchemy import Column, Integer, String, create_engine, Sequence, ForeignKey, DateTime, Text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from companycodegeneretor import generate_company_code
from datetime import datetime
from pgvector.sqlalchemy import Vector

DATA_BASE_URL =("postgresql://postgres:abdullah123@localhost:5432/ai_assistant")

engine =create_engine(DATA_BASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()

class Companies(base):
    __tablename__ = "companies"

    id = Column(Integer, Sequence('companies_id_seq'), primary_key=True)
    name = Column(String(50))
    business_type = Column(String(50))
    email = Column(String)
    contactnumber = Column(String(20))
    companycode = Column(String(20), unique=True, default=generate_company_code())
    registerd_at = Column(
        DateTime,
        default=datetime.now
    )


class CompaniesData(base):

    __tablename__ = "companies_data"

    id = Column(Integer, primary_key=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id")
    )

    file_name = Column(String(255))

    file_type = Column(String(50))

    file_path = Column(String(500))

    content = Column(Text)

    uploaded_at = Column(
        DateTime,
        default=datetime.now
    )

base.metadata.create_all(engine)
session.commit()