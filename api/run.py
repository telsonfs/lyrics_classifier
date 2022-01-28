from flask import Flask
from flask import jsonify
from flask import request
import json


from nlp.model.model import Model
from flask import render_template
import pandas as pd


from forms.lyrics_form import LyricForm


model = Model()

app = Flask(__name__)
app.config['SECRET_KEY']  = 'codigo_de_seguranca'

@app.route("/", methods=['GET', 'POST'])
def classifier_form():
    form = LyricForm()

    if form.validate_on_submit():
        result = model.lyric_classifier(form.lyric.data)
        return result[0]
    return render_template('lyric_form.html', form=form)

@app.route("/classifier_lyrics", methods=['POST'])
def classifier_api():
    data = request.get_json()
    result = model.lyric_classifier(data["lyric"])
    return jsonify(result[0])


if __name__ == '__main__':
    app.run()