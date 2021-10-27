from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route('/')
def generate_story():
    prompts = story.prompts

    return render_template("generate.html", prompts=prompts)


@app.route('/story')
def your_Story():

    text = story.generate(request.args)

    return render_template("story.html", text=text)
