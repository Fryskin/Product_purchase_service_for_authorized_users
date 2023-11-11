from datetime import datetime
from sqlalchemy import Table, Column, String, Integer, TIMESTAMP, Boolean

from src.database import metadata

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow,),
    Column("updated_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True),
)
