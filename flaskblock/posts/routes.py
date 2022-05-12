from flask import request, render_template, Blueprint, redirect, flash, url_for, abort
from flask_login import login_required, current_user
from flaskblock.models import Post
from flaskblock.posts.forms import PostForm
from flaskblock import db

posts = Blueprint('posts', __name__)

@posts.route('/post/new/', methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user.username, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()        
        flash('Your post has been created', 'success')
        return redirect(url_for('main.home'))    
    return render_template('create_post.html', title = 'New Post', 
                            form = form, legend='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post = post)


@posts.route('/post/<int:post_id>/update/', methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user.username:
        print(current_user)
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', 
                            form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete/', methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user.username:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('main.home'))
