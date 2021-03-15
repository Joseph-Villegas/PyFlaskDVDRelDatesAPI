"""
Filename: app.py
Abstract: A flask api that performs a web 
          scrape to retrieve current dvd release information
"""
from flask import Flask, jsonify
from scraper import scrape, search_by_week

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>DVD Release Dates API</h1> \
        <p>This API retrieves retail release schedules for DVDs by performing a web scrape</p> \
        <p>Source: https://www.dvdsreleasedates.com</p> \
        <p>Try these endpoints: /this-week, /last-week, /next-week, /in-two-weeks, /all-weeks</p>"

@app.route('/last-week', methods=['GET'])
def last_week():
    scrape_results = search_by_week('last week')
    return jsonify({'scrape_results': scrape_results, 'num_weeks': len(scrape_results)})

@app.route('/this-week', methods=['GET'])
def this_week():
    scrape_results = search_by_week('this week')
    return jsonify({'scrape_results': scrape_results, 'num_weeks': len(scrape_results)})

@app.route('/next-week', methods=['GET'])
def next_week():
    scrape_results = search_by_week('next week')
    return jsonify({'scrape_results': scrape_results, 'num_weeks': len(scrape_results)})

@app.route('/in-two-weeks', methods=['GET'])
def in_two_weeks():
    scrape_results = search_by_week('in 2 weeks')
    return jsonify({'scrape_results': scrape_results, 'num_weeks': len(scrape_results)})

@app.route('/all-weeks', methods=['GET'])
def all_weeks():
    scrape_results = scrape()
    return jsonify({'scrape_results': scrape_results, 'num_weeks': len(scrape_results)})

if __name__ == "__main__":
    app.run()
