from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import web_scraping

app= Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    
    mars_data = mongo.db.information.find_one()
        # Return template and data
    return render_template("index.html", mars=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function

    mars_data = web_scraping.web_scraping()

    # Update the Mongo database using update and upsert=True
    mongo.db.information.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
