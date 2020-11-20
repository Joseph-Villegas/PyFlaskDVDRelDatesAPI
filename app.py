"""
Filename: app.py
Abstract: A flask api that performs a web 
          scrape to retrieve current dvd release dates
"""
from flask import Flask, jsonify
from dvd_bot import DVDBot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'


@app.route('/', methods=['GET'])
def home():
    return "<h1>DVD Release Dates API</h1> \
        <p>This API retrieves retail release schedules for DVDs by performing a web scrape</p> \
        <p>Source: https://www.dvdsreleasedates.com</p> \
        <p>Try these endpoints: /this-week, /last-week, /next-week, /in-two-weeks</p>"


@app.route('/last-week', methods=['GET'])
def lastWeek():
    Bot = DVDBot()
    week, dvds = Bot.getReleasesByWeek(1)
    return jsonify({'weekOf': week, 'releases': dvds})


@app.route('/this-week', methods=['GET'])
def thisWeek():
    Bot = DVDBot()
    week, dvds = Bot.getReleasesByWeek(2)
    return jsonify({'weekOf': week, 'releases': dvds})


@app.route('/next-week', methods=['GET'])
def nextWeek():
    Bot = DVDBot()
    week, dvds = Bot.getReleasesByWeek(3)
    return jsonify({'weekOf': week, 'releases': dvds})


@app.route('/in-two-weeks', methods=['GET'])
def inTwoWeeks():
    Bot = DVDBot()
    week, dvds = Bot.getReleasesByWeek(0)
    return jsonify({'weekOf': week, 'releases': dvds})


if __name__ == "__main__":
    app.run()
