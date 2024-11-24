from flask import Flask
import random


ran_num=random.randint(0,10)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>guess a number between 0 to 10 </p><iframe src="https://giphy.com/embed/4JVTF9zR9BicshFAb7" width="480" height="346" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/achievementhunter-rooster-teeth-achievement-hunter-off-topic-ah-4JVTF9zR9BicshFAb7">via GIPHY</a></p>'


@app.route("/<guess>")
def highLow(guess):
    if int(guess)<ran_num:
        return '<iframe src="https://giphy.com/embed/IevhwxTcTgNlaaim73" width="480" height="269" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/gsimedia-lowrider-gsi-chevytruck-IevhwxTcTgNlaaim73">via GIPHY</a></p>'
    if int(guess)>ran_num:
        return '<iframe src="https://giphy.com/embed/27sdoZn8YhLbil01q6" width="480" height="271" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/johnlegend-john-legend-so-high-27sdoZn8YhLbil01q6">via GIPHY</a></p>'
    if int(guess)==ran_num:
        return '<iframe src="https://giphy.com/embed/y6Inkaz7omxAk" width="480" height="355" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/walter-white-y6Inkaz7omxAk">via GIPHY</a></p>'


if __name__=="__main__":
    app.run(debug=True)

