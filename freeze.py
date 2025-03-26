from flask_frozen import Freezer
from funder_site.app import app

freezer = Freezer(app)

if __name__ == '__main__':
    print(list(freezer.all_urls()))
    freezer.freeze()
    print("Frozen!")