from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class TodoTaskForm(FlaskForm):
    title = StringField('Titel', validators=[DataRequired(), Length(max=128)])
    deadline = DateField('Fälligkeitsdatum', format='%Y-%m-%d', validators=[Optional()])
    status = SelectField('Status', choices=[('Offen', 'Offen'), ('In Bearbeitung', 'In Bearbeitung'), ('Erledigt', 'Erledigt')], validators=[DataRequired()])
    comment = TextAreaField('Kommentar', validators=[Optional(), Length(max=512)])
    submit = SubmitField('Aufgabe hinzufügen')
