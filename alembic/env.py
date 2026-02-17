from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Import your app's config and Base model
from app.core.config import settings
from app.db.base import Base

# This is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 1. Set the target metadata so 'autogenerate' works
target_metadata = Base.metadata

# 2. Force the URL to be the one from your .env file
config.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URI)
