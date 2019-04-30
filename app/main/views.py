from flask import render_template,request,redirect,url_for, abort
from flask_login import login_required, current_user
from . import main
from .. import db, photos
import markdown2



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Moringa Pitch'
    return render_template('index.html', title = title)

@main.route('/comment/new/<int:post_id>', methods = ['GET','POST'])
@login_required
def new_comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)

    if form.validate_on_submit():
        comment = form.comment.data
         
        # Updated comment instance
        new_comment = Comment(comment=comment,user_c=current_user._get_current_object().id, post_id=post_id)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.new_comment',post_id = post_id ))

    all_comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('comment.html', form=form, comments=all_comments, post=post)

@main.route('/post/star/<int:post_id>/star', methods=['GET', 'POST'])
@login_required
def star(post_id):
    post = Post.query.get(post_id)
    user = current_user
    post_stars = Star.query.filter_by(post_id=post_id)
    posts = Post.query.order_by(Post.posted_p.desc()).all()

    if Star.query.filter(Star.user_id == user.id, Star.post_id == post_id).first():
        return render_template('posts.html', posts=posts)

    new_star = Star(post_id=post_id, user=current_user)
    new_star.save_stars()
    
    return render_template('posts.html', posts=posts)