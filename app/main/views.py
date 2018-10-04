from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from app.models import Category,Project
from flask_login import login_required, current_user
from .forms import CategoryForm,ProjectForm

@main.route('/')
def index():
    categories = Category.get_categories()
    return render_template('index.html',categories=categories)

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

@main.route('/category/<int:id>')
def category(id):
    category = Category.load_category(id)
    projects = category.projects()
    return render_template('main/category.html',projects=projects)

@main.route('/new_project', methods=['GET','POST'])
@login_required
def new_project():
    categories = [(c.id, c.name) for c in Category.get_categories()]
    form = ProjectForm(request.form)
    form.category.choices = categories
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        category = form.category.data

        new_project = Project(title=title, description=description,
                        user_id = current_user.id,category=category)
        new_project.save_project()
        return redirect(url_for('.index'))
    return render_template('main/new_project.html', project_form=form)