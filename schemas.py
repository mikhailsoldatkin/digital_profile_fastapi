from _pydecimal import Decimal
from datetime import date
from typing import Optional, List

from pydantic import BaseModel, field_serializer, Field

from constants import CITIZENSHIP, UNIT_TYPES, DOC_TYPES, UNIT_STATUS_CHOICES


class Document(BaseModel):
    type: int
    series: str
    number: str
    issuer: Optional[str]
    date: Optional[date]

    class Config:
        from_attributes = True

    @field_serializer('type')
    def type(self, type: int):
        return DOC_TYPES.get(type)


class PersonDocument(BaseModel):
    id: int
    person_id: int
    document_id: int

    class Config:
        from_attributes = True


class Address(BaseModel):
    full: str

    class Config:
        from_attributes = True


class Person(BaseModel):
    firstname: str
    patronymic: Optional[str]
    surname: str
    fullname: str
    date_of_birth: date
    snils: Optional[str]
    gender: int
    citizenship: int
    documents: Optional[List[Document]]
    act_address: Optional[Address]

    class Config:
        from_attributes = True

    @field_serializer('citizenship')
    def citizenship(self, citizenship: int):
        return CITIZENSHIP.get(citizenship)

    @field_serializer('gender')
    def gender(self, gender: int):
        return 'Мужской' if gender == 1 else 'Женский'

    @field_serializer('fullname')
    def fullname(self, fullname: str):
        if self.patronymic:
            return f'{self.surname} {self.firstname} {self.patronymic}'
        return f'{self.surname} {self.firstname}'


class Employee(BaseModel):
    person: Person
    employment_date: date
    dismissal_date: Optional[date]
    rate: Optional[Decimal]

    class Config:
        from_attributes = True


class Unit(BaseModel):
    short_name: str
    director: Optional[Employee]
    type_id: int = Field(serialization_alias='type')
    kind_id: Optional[int] = Field(serialization_alias='kind')
    org_status: int
    area_type_id: int = Field(serialization_alias='area_type')

    class Config:
        from_attributes = True

    @field_serializer('type_id')
    def type(self, type_id: int):
        return UNIT_TYPES.get(type_id)

    @field_serializer('org_status')
    def org_status(self, org_status: int):
        UNIT_STATUSES = {k: v for k, v in UNIT_STATUS_CHOICES}
        return UNIT_STATUSES.get(org_status)
