import click
from movieReview import app, db
from movieReview.models import Record
import random
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
            mark=random.randint(8, 10)
        )
        print(record)
        db.session.add(record)
    db.session.commit()

    click.echo('Generated %d reviews for the movie.' % count)

# forge(10)