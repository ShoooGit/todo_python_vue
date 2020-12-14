from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

# postgresqlのDB設定
# "postgresql://{DBのユーザ}:{DBのパスワード}@{url}:{ポート番号}/{DB名}"
DATABASE = "postgresql://postgres:@192.168.43.32:5432/todo_flask"

# Engineの作成
ENGINE = create_engine(
  DATABASE,
  encoding="utf-8",
  # TrueにするとSQLが実行される度に出力される
  echo=True
)

# Sessionの作成
session = scoped_session(
  # ORM実行時の設定。自動コミットするか、自動反映するかなど。
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
  )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()