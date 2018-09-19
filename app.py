# using python 3
import socket
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

"""FILL IN INFORMATION HERE"""

class_name = "2DM3 T04" #FILL IN YOUR TUTORIAL NUMBER
ta_name = "Sophia Tao" #FILL IN YOUR NAME
ta_email = "email@example.com" #FILL IN YOUR EMAIL

""" YOU SHOULD NOT HAVE TO CHANGE ANYTHING BELOW THIS POINT"""

info_header = "Theorems"
comments = []
info_file = "Resources/theorems.txt"

def get_info_data():
    with open(info_file) as f:
        return f.read().splitlines()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some?bamboozle#string-foobar'
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

class NameForm(FlaskForm):
    comment = StringField('Comment', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    form = NameForm()
    comment = form.comment.data
    changed = False

    if form.validate_on_submit():
        comments.insert(0, comment)
        changed = True
        form.comment.data = ""

    return render_template('index.html',
        form=form,
        comments=comments,
        info_data=get_info_data(),
        class_name=class_name,
        ta_name=ta_name,
        ta_email=ta_email,
        info_header=info_header,
        )

if __name__ == '__main__':
    print("Make connections to: " + socket.gethostbyname(socket.gethostname()))
    print("Port: 5000")
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0')
