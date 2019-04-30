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

@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch = Post.query.get(pitch_id)

    if form.validate_on_submit():
        comment = form.comment.data
         
        # Updated comment instance
        new_comment = Comment(comment=comment,user_c=current_user._get_current_object().id, pitch_id=pitch_id)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.new_comment',pitch_id = pitch_id ))

    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    return render_template('comment.html', form=form, comments=all_comments, pitch=pitch)

@main.route('/pitch/star/<int:pitch_id>/star', methods=['GET', 'POST'])
@login_required
def star(pitch_id):
    pitch = Post.query.get(pitch_id)
    user = current_user
    pitch_stars = Star.query.filter_by(pitch_id=pitch_id)
    pitchs = Post.query.order_by(Post.pitched_p.desc()).all()

    if Star.query.filter(Star.user_id == user.id, Star.pitch_id == pitch_id).first():
        return render_template('pitchs.html', pitchs=pitchs)

    new_star = Star(pitch_id=pitch_id, user=current_user)
    new_star.save_stars()
    
    return render_template('pitchs.html', pitchs=pitchs)