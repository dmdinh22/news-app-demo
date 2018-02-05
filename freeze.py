from flask_frozen import Freezer
from app import app, get_csv
freezer = Freezer(app)

@freezer.register_generator
def detail():
    # iterate over all rows from get_csv method
    for row in get_csv():
        # make page for each id
        yield {'row_id': row['id']}

if __name__ == '__main__':
    freezer.freeze()
