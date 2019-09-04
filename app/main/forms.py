from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField('Category name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    title = StringField('Project name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = SelectField('Category', choices=[], coerce=int)
    submit = SubmitField('Submit')