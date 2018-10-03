from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from app.models import Category
from flask_login import login_required, current_user
from .forms import CategoryForm

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/new_category', methods=['GET','POST'])
@login_required
def new_category():
    form = CategoryForm()  
    if form.validate_on_submit():
        name = form.name.data

        new_category=Category(name=name)

        new_category.save_category()
        return redirect(url_for('.index'))
    
    return render_template('main/new_category.html', category_form=form)