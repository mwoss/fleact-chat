from fleactchat import app
from flask import render_template

# render_template
# @app.errorhandler(404)
# def page_not_found():
#     return render_template('page_not_found.html'), 404


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
