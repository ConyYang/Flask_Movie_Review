from flask import flash, redirect, url_for, render_template

from movieReview import app, db
from movieReview.models import Record
from movieReview.forms import ReviewForm

@app.route('/', methods=['GET', 'POST'])
def index():
    records = Record.query.order_by(Record.timestamp.desc()).all()
    myform = ReviewForm()
    if myform.validate_on_submit():
        username = myform.username.data
        review = myform.review.data
        mark = myform.mark.data
        new_record = Record(username=username, review=review, mark=mark)
        db.session.add(new_record)
        db.session.commit()
        flash('Your review to the movie has been updated !')
        return redirect(url_for('index'))
    return render_template('index.html', myform=myform, records=records)
