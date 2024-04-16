from flask import Blueprint, render_template, redirect, url_for
from .forms import PostForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Logic to retrieve and display posts
    return render_template('index.html')

@main.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        # Logic to create a new post
        return redirect(url_for('main.index'))
    return render_template('create_post.html', title='Create Post', form=form)
