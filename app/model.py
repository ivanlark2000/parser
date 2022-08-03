from app.config import config
from sqlalchemy import create_engine
from sqlalchemy import BIGINT, DECIMAL
from sqlalchemy import Column, Integer, String, Sequence, TIMESTAMP, VARCHAR, ForeignKey, Text, Numeric, Boolean
from sqlalchemy.orm import relation

Base = config.Base


class Flat(Base):
    __tablename__ = "flat"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_avito = Column(BIGINT)
    number = Column(Integer)
    price = Column(Numeric(12, 1), nullable=False)
    qty_of_rooms = Column(Integer)
    total_space = Column(Numeric(3, 1), nullable=False)
    square_of_kitchen = Column(Numeric(3, 1), nullable=False)
    living_space = Column(Numeric(3, 1), nullable=False)
    floor = Column(Integer, nullable=False)
    furniture = Column(String(200))
    technics = Column(String(200))
    balcony_or_loggia = Column(String(120))
    room_type = Column(String(120))
    ceiling_height = Column(Numeric(3, 1))
    bathroom = Column(String(120))
    window = Column(String(120))
    repair = Column(String(120))
    seilling_method = Column(String(120))
    transaction_type = Column(String(120))
    decorating = Column(String(120))
    warm_floor = Column(Boolean)
    seller = Column(String(120))
    type_seller = Column(String(200))
    description = Column(Text)
    time_of_add = Column(TIMESTAMP, nullable=False)
    status = Column(Integer, ForeignKey('sailing_status.id'), nullable=False)
    house_id = Column(Integer, ForeignKey('house.id'), nullable=False)


class House(Base):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True, autoincrement=True)
    obl = Column(String(150))
    street = Column(String(200), nullable=False)
    city = Column(String(150))
    number_of_house = Column(String(50))
    new_building_name = Column(String(200))
    offical_builder = Column(String(200))
    year_of_construction = Column(Integer)
    floors_in_the_house = Column(Integer)
    type_of_home = Column(String(150))
    passenger_bodice = Column(String(100), nullable=False)
    service_lift = Column(String(100), nullable=False)
    in_home = Column(String(200))
    yard = Column(Text)
    parking = Column(Text)
    deadline = Column(String(150))
    street_id = Column(Integer, ForeignKey('street.id'), nullable=False)


class Street(Base):
    __tablename__ = 'street'

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(155), nullable=False)
    district_id = Column(Integer, ForeignKey('district.id'), nullable=False)


class District(Base):
    __tablename__ = 'district'

    id = Column(Integer, primary_key=True, autoincrement=True)
    district = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(155), nullable=False)
    obl_id = Column(Integer, ForeignKey('obl.id'), nullable=False)


class Obl(Base):
    __tablename__ = 'obl'

    id = Column(Integer, primary_key=True, autoincrement=True)
    obl = Column(String(155), nullable=False)


class Active_flat(Base):
    __tablename__ = 'active_flat'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number_author = Column(Integer)
    id_in_site = Column(Integer)
    site_id = Column(Integer, ForeignKey('where_download.id'), nullable=False)


class Site(Base):
    __tablename__ = 'where_download'

    id = Column(Integer, primary_key=True, autoincrement=True)
    site = Column(String(100), nullable=False)


class Status(Base):
    __tablename__ = 'sailing_status'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(100), nullable=False)

