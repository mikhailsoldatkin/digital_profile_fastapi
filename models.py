import os
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import String, Date, ForeignKey, Numeric, create_engine, Column, Integer
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, Mapped, mapped_column

load_dotenv()

postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_db = os.getenv('POSTGRES_DB_NAME')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

DB_URL = f'postgresql://{postgres_user}:{postgres_password}@{db_host}:{db_port}/{postgres_db}'
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class AddressModel(Base):
    __tablename__ = 'core_address'

    id = Column(Integer, primary_key=True, index=True)
    full = Column(String)
    person_act = relationship('PersonModel', back_populates='act_address')


class DocumentModel(Base):
    __tablename__ = 'core_document'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer)
    series = Column(String)
    number = Column(String)
    issuer = Column(String)
    date = Column(Date)

    person_documents = relationship('PersonDocumentModel', back_populates='document', viewonly=True)
    persons = relationship('PersonModel', secondary='person_persondocument', back_populates='documents', viewonly=True)


class PersonDocumentModel(Base):
    __tablename__ = 'person_persondocument'

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('person_person.id'))
    person = relationship('PersonModel', back_populates='person_documents', viewonly=True)

    document_id: Mapped[int] = mapped_column(ForeignKey('core_document.id'))
    document = relationship('DocumentModel', back_populates='person_documents', viewonly=True)


class PersonModel(Base):
    __tablename__ = 'person_person'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    patronymic = Column(String)
    surname = Column(String)
    date_of_birth = Column(Date)
    snils = Column(String)
    citizenship: Mapped[Optional[int]]
    gender: Mapped[int]

    employee = relationship('EmployeeModel', back_populates='person')
    person_documents = relationship('PersonDocumentModel', back_populates='person')
    documents = relationship(
        'DocumentModel',
        secondary='person_persondocument',
        back_populates='persons',
        viewonly=True
    )
    act_address_id = Column(Integer, ForeignKey('core_address.id'))
    act_address = relationship('AddressModel', back_populates='person_act')


class EmployeeModel(Base):
    __tablename__ = 'employee_employee'

    id = Column(Integer, primary_key=True, index=True)
    employment_date = Column(Date)
    dismissal_date = Column(Date, nullable=True)
    rate = Column(Numeric, nullable=True)

    person_id = Column(Integer, ForeignKey('person_person.id'))
    person = relationship('PersonModel', back_populates='employee')

    unit = relationship('UnitModel', back_populates='director')


class UnitModel(Base):
    __tablename__ = 'unit_unit'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    short_name: Mapped[str]
    full_name: Mapped[str]
    type_id: Mapped[int]
    kind_id: Mapped[Optional[int]]
    org_status: Mapped[int]
    area_type_id: Mapped[int]

    director_id: Mapped[int] = mapped_column(ForeignKey('employee_employee.id'))
    director: Mapped['EmployeeModel'] = relationship(back_populates='unit')
