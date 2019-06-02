import pandas as pd


import os
print(os.environ)
import config
# if os.environ[]
#     config
# print(config.name)

# import numpy as np

# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy



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


