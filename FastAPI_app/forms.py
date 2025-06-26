from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField("タイトル", validators=[DataRequired()])
    description = TextAreaField("詳細")
    deadline = DateField("締切日", format='%Y-%m-%d')
    completed = BooleanField("完了")
    submit = SubmitField("保存")