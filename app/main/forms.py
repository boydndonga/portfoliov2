from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class CategoryForm(FlaskForm):
    name = StringField('Category name', validators=[Required()])
    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    title = StringField('Project name', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    category = SelectField('Category', choices=[], coerce=int)
    submit = SubmitField('Submit')