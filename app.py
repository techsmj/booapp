import pandas as pd

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlalchemy.dialects.sqlite

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

import os
print(os.environ)

if not os.environ.get("DYNO"):
    import config
    print(config.name)


if os.environ.get("JAWSDB_URL"):
    dburl = os.environ["JAWSDB_URL"]
else:
    dburl = "sqlite://"
   
engine = sqlalchemy.create_engine(dburl)
df= pd.read_sql("SELECT * FROM belly_button_metadata", engine)
print(df)

app = Flask(__name__)

@app.route("/")
def home():
    """Return the homepage."""
    return render_template("index.html")
 


@app.route("/data")
def data():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    # stmt = db.session.query(Samples).statement
    # df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify({"data":" is empty"})

if __name__ == "__main__":
    app.run()


