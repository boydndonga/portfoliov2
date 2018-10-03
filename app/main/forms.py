from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class CategoryForm(FlaskForm):
    name = StringField('Category name', validators=[Required()])
    submit = SubmitField('Submit')