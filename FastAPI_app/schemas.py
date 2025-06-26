from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# スキーマの定義
class TaskBase(BaseModel):
    # TODO：タイトルは必須項目とし、入力文字数は1～10文字となるように設定して下さい
    title: str = Field(..., min_length=1, max_length=10, description="タイトルは1～10文字")
    
    # TODO：詳細の入力文字数は最大100文字までとなるように設定して下さい
    description: Optional[str] = Field(None, max_length=100, description="詳細は最大100文字まで")
    
    # TODO：締切日はYYYY-MM-DD形式となるように設定して下さい
    deadline: Optional[date] = Field(None, description="締切日はオプション（日付フォーマット: YYYY-MM-DD）")

    # TODO：完了フラグはデフォルト値がfalseとなるように設定して下さい
    completed: bool = Field(False, description="完了フラグ（True/False）")

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        from_attributes=True