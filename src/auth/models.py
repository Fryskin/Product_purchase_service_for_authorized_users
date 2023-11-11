from datetime import datetime
from pydantic import PydanticUserError, field_validator

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from pydantic import ValidationError
from sqlalchemy import Table, Column, Integer, \
    String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

from src.database import metadata

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, ),
    Column("email", String, nullable=False, unique=True),
    Column("username", String, nullable=False),
    Column("phone_number", String, nullable=True, unique=True),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)
    phone_number = Column(String, nullable=True, unique=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))

    hashed_password: Mapped[str] = mapped_column(String(
                                                 length=1024),
                                                 nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean,
                                            default=True,
                                            nullable=False)

    is_superuser: Mapped[bool] = mapped_column(Boolean,
                                               default=False,
                                               nullable=False)

    is_verified: Mapped[bool] = mapped_column(Boolean,
                                              default=False,
                                              nullable=False)

    try:
        @field_validator('phone_number')
        def validator(self, values: str):
            min_phone_length = 9
            max_phone_length = 16
            first_char = '+'
            if values[0] == first_char and\
                    min_phone_length <= len(values) <= max_phone_length:
                return f'Phone number: {values}'

            else:
                raise ValidationError

    except PydanticUserError as exc_info:
        assert exc_info.code == 'validator-instance-method'
