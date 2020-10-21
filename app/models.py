from sqlalchemy import DateTime, Integer, String, Text, MetaData, Column, Table, create_engine
from datetime import datetime
from app.load_conf import load_config


config = load_config()['sqlalchemy']
engine = create_engine(config)

metadata = MetaData()

user = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, unique=True),
    Column("name", String),
    Column("last_name", String),
    Column("email", Text, unique=True),
    Column("phone", Text),
    Column("add_time", DateTime, default=datetime.now()),
)

item = Table(
    "items", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("price", String),
)

metadata.create_all(engine)
