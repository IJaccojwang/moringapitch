from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . import main
from .forms import PitchForm, CommentForm
from ..models import Pitch, Comment
from .. import db
import markdown2


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Moringa Pitch'
    pitches = Pitch.query.order_by(Pitch.pitched_p.desc()).all()
    return render_template('index.html', title = title, pitch = pitch)

@main.route('/pitches')
def pitches():
    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.order_by(Pitch.pitched_p.desc()).all()
    return render_template('pitches.html', pitches=pitches)

@main.route('/pitch/<int:id>')
def pitch(id):

    '''
    View movie page function that returns the pitch details page and its data
    '''
    pitches = Pitch.query.filter_by(id=id)
    comments = Comment.query.filter_by(pitch_id=id).all()

    return render_template('pitch.html',pitches = pitches,comments = comments)

@main.route('/pitch/new', methods=['GET', 'POST'])
def new_pitches():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        github_link = form.github_link.data

        new_pitch = Pitch(title=title, description=description,
                          github_link=github_link)
        new_pitch.save_pitch()

    title = 'New Pitch'
    return render_template('new_pitch.html', title=title, pitch_form=form)

@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)

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
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_stars = Star.query.filter_by(pitch_id=pitch_id)
    pitches = Pitch.query.order_by(Pitch.pitched_p.desc()).all()

    if Star.query.filter(Star.user_id == user.id, Star.pitch_id == pitch_id).first():
        return render_template('pitches.html', pitches=pitches)

    new_star = Star(pitch_id=pitch_id, user=current_user)
    new_star.save_stars()
    
    return render_template('pitches.html', pitches=pitches)
    return render_template('index.html', title=title)






