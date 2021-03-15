# PyFlaskDVDRelDatesAPI

**PyFlaskDVDRelDatesAPI** is a REST api that performs a webscrape to deliver current DVD release information. The api is implemented in the Python programming language using the flask module, the information is collected after a web scrape done using the beautiful soup package.

DVD information is scraped from this site: https://www.dvdsreleasedates.com
The api is hosted on Heroku here: https://dvd-release-dates.herokuapp.com/

Some api endpoints for your viewing:
- /this-week
- /next-week
- /last-week
- /in-two-weeks
- /all-weeks

NOTE: All endpoints provide a response, however, the response may or may not include DVD release information of their is no information for that week on the source site.

## Packages used
- flask
- requests
- bs4
