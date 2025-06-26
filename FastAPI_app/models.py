from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# データベースの接続URLを設定
DATABASE_URL = "sqlite:///./app.db"

# SQLAlchemyのエンジンを作成
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# セッションを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baseクラスを定義
Base = declarative_base()

# DBモデルの定義
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    deadline = Column(Date, nullable=True)
    completed = Column(Boolean, default=False)