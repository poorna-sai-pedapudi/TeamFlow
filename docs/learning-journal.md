Day X

1. What did I build?

2. What backend concept did I learn?

3. What production lesson did I learn?

4. What interview question can I now answer?

5. What confused me today?

6. What is the difference between SQLAlchemy and Alembic?
SQLAlchemy is the ORM/toolkit that lets your Python code define models and query the database at runtime. Alembic is the migration tool that tracks and applies incremental changes to the database schema over time (create table, add column, etc.) — it uses SQLAlchemy's metadata to generate those migrations but only runs when you explicitly migrate, not during normal app operation.

7. Why do we separate config.py and database.py?
config.py holds settings (where to find the DB, what credentials to use) sourced from the environment — it's just data. database.py holds the engine/session setup that uses those settings to actually connect. Separating them means the connection logic doesn't care where database_url came from, and the settings can be reused/tested independently of any DB connection being made.