import click
from movieReview import app, db
from movieReview.models import Record

@app.cli.command()
@click.option('--count', default=10, help='Random 10 reviews')
def forge(count):
    from faker import Faker
    db.drop_all()
    db.create_all()

    faker = Faker()
    click.echo('Generating...')

    for i in range(count):
        record = Record(
            username=faker.name(),
            review=faker.sentence(),
            timestamp=faker.date_time_this_year(),
            mark=faker.random.number({min: 8, max: 10})
        )
        db.session.add(record)
    db.session.commit()

    click.echo('Generated %d reviews for the movie.' % count)