from flask import Flask, render_template, make_response, url_for
from data import tours, departures

app = Flask(__name__)


@app.route('/')
def main():
    tour = tours
    return render_template('main.html', tours=tour)


@app.route('/from/<direction>/')
def direction(direction):
    if direction in departures:
        idlist = dict((title['title'], id) for id, title in tours.items())
        tour = list(tour for tour in tours.values() if tour['departure'] == direction)
        return render_template('direction.html', tours=tour, direction=direction, departures=departures, id=idlist)
    return make_response("<p>HTTP 404 Error Encountered</p>", 404)


@app.route('/tours/<id>/')
def tour(id):
    tour = tours[int(id)]
    return render_template('tour.html', tour=tour, departures=departures)


@app.errorhandler(404)
def not_found(e):
    return "<p>HTTP 404 Error Encountered</p>"


if __name__ == '__main__':
    app.run()
