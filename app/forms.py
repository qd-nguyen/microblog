from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class TodoTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=128)])
    deadline = DateField('Deadline', validators=[Optional()])
    status = SelectField('Status', choices=[('offen', 'Offen'), ('erledigt', 'Erledigt')], validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[Optional(), Length(max=512)])
    submit = SubmitField('Hinzufügen')