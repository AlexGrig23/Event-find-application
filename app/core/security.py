import os
from datetime import datetime, timedelta

import jwt

from fastapi.security import APIKeyHeader
from passlib.context import CryptContext




password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
apikey_scheme = APIKeyHeader(name="Authorization")
