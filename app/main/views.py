from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . import main
from .forms import PitchForm
from ..models import Pitch
from .. import db, photos
import markdown2


pitch = [
    {
        'title': 'Invention',
        'description': 'Created for us',
        'github_link': 'github.com'
    },
    {
        'title': 'Invention',
        'description': 'Created for us',
        'github_link': 'github.com'
    }
]


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Moringa Pitch'
    return render_template('index.html', title=title)


@main.route('/pitches')
def pitches():
    '''
    View root page function that returns the index page and its data
    '''
    pitch = Pitch.get_pitches('1')
    return render_template('pitch.html', pitch=pitch)


@main.route('/new_pitches', methods=['GET', 'POST'])
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
