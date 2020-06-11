from flask import flash, redirect, url_for, render_template
from sqlalchemy import func

from movieReview import app, db
from movieReview.models import Record
from movieReview.forms import ReviewForm


@app.route('/', methods=['GET', 'POST'])
def index():
    records = Record.query.order_by(Record.timestamp.desc()).all()
    mark_raw = Record.query.with_entities(func.avg(Record.mark)).all()
    mark = round(mark_raw[0][0],1)
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
    return render_template('index.html', myform=myform, records=records, mark=mark)
