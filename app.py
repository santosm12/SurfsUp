# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import re

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "#################################################\n",
    "# Flask Routes\n",
    "#################################################\n",
    "\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    \"\"\"List all available api routes.\"\"\"\n",
    "    return (\n",
    "        f\"Avalable Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations</br>\"\n",
    "        f\"/api/v1.0/tobs</br>\"\n",
    "        f\"/api/v1.0/<start><br>\"\n",
    "        f\"/api/v1.0/<start>/<end></br>\"\n",
    "        )\n",
    "\n",
    "## /api/v1.0/precipitation\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    \"\"\"return a list of the dates and precipitation from the last year\"\"\"\n",
    "# Query for the dates and precipitation from the last year.\n",
    "    results = session.query(Measurement.date, Measurement.prcp).\\\n",
    "    filter(Measurement.date > '2016-08-23').\\\n",
    "    order_by(Measurement.date).all()\n",
    "\n",
    "# Convert the query results to a Dictionary using date as the key \n",
    "# and prcp as the value.\n",
    "    precipitations = []\n",
    "    for result in results:\n",
    "        row = {}\n",
    "        row[\"date\"] = result[0]\n",
    "        row[\"prcp\"] = float(result[1])\n",
    "        precipitation.append(row)\n",
    "\n",
    "    return jsonify(precipitations)\n",
    "\n",
    "# Return the json representation of your dictionary.\n",
    "\n",
    "## /api/v1.0/stations\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "# Return a json list of stations from the dataset.\n",
    "def stations():\n",
    "    \"\"\"Return a list of stations \"\"\"\n",
    "    #Query all stations\n",
    "    results = session.query(Stations.name).all()\n",
    "\n",
    "    #Convert list of tuples into normal list\n",
    "    all_stations = list(np.ravel(results))\n",
    "\n",
    "    return jsonify(all_stations)\n",
    "## /api/v1.0/tobs\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def temperature():\n",
    "    \"\"\"return a list of temperatures from the last year\"\"\"\n",
    "# Return a json list of Temperature Observations (tobs) for the \n",
    "# previous year\n",
    "# Query for the dates and temperatures from the last year.\n",
    "    results = session.query(Measurement.tobs, Measurement.date).\\\n",
    "    filter(Measurement.date > '2016-08-23').\\\n",
    "    order_by(Measurement.date).all()\n",
    "# Convert the query results to a Dictionary using date as the key \n",
    "# and prcp as the value.\n",
    "    temperatures = []\n",
    "    for result in results:\n",
    "        row = {}\n",
    "        row[\"date\"] = result[0]\n",
    "        row[\"tobs\"] = float(result[1])\n",
    "        temperatures.append(row)\n",
    "\n",
    "    return jsonify(temperatures)\n",
    "## /api/v1.0/<start> and /api/v1.0/<start>/<end>\n",
    "\n",
    "# Return a json list of the minimum temperature, the average temperature, \n",
    "# and the max temperature for a given start or start-end range.\n",
    "\n",
    "# When given the start only, calculate TMIN, TAVG, and TMAX for all dates \n",
    "# greater than and equal to the start date.\n",
    "\n",
    "# When given the start and the end date, calculate the TMIN, TAVG, and \n",
    "# TMAX for dates between the start and end date inclusive.\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}