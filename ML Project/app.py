import pandas
from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    price_pred = 0
    
    if request.method == "POST":
        # Get the Input Values:
        generation_biomass = request.form["generation_biomass"]
        generation_lignite = request.form["generation_lignite"]
        generation_fossil_gas = request.form["generation_fossil_gas"]
        generation_fossil_hard_coal = request.form["generation_fossil_hard_coal"]
        generation_fossil_oil = request.form["generation_fossil_oil"]
        generation_hydro_pump = request.form["generation_hydro_pump"]
        generation_river_runoff = request.form["generation_river_runoff"]
        generation_hydro_water = request.form["generation_hydro_water"]
        generation_nuclear = request.form["generation_nuclear"]
        generation_other = request.form["generation_other"]
        generation_other_renew = request.form["generation_other_renew"]
        generation_solar = request.form["generation_solar"]
        generation_waste = request.form["generation_waste"]
        generation_wind_onshore = request.form["generation_wind_onshore"]
        forecast_solar_day = request.form["forecast_solar_day"]
        forecast_wind_day = request.form["forecast_wind_day"]
        forecast_total_load = request.form["forecast_total_load"]
        actual_total_load = request.form["actual_total_load"]
        price_day_ahead = request.form["price_day_ahead"]

        # Create a PandaS DataFrame from the Input Values:
        labels = ["generation_biomass", "generation_lignite", "generation_fossil_gas",
                  "generation_fossil_hard_coal", "generation_fossil_oil",
                  "generation_hydro_pump", "generation_river_runoff", "generation_hydro_water",
                  "generation_nuclear", "generation_other", "generation_other_renew",
                  "generation_solar", "generation_waste", "generation_wind_onshore",
                  "forecast_solar_day", "forecast_wind_day", "forecast_total_load",
                  "actual_total_load", "price_day_ahead"]

        row = [[generation_biomass, generation_lignite, generation_fossil_gas, generation_fossil_hard_coal,
                 generation_fossil_oil, generation_hydro_pump, generation_river_runoff, generation_hydro_water,
                 generation_nuclear, generation_other, generation_other_renew, generation_solar,
                 generation_waste, generation_wind_onshore, forecast_solar_day, forecast_wind_day,
                 forecast_total_load, actual_total_load, price_day_ahead]]

        data = pandas.DataFrame(data=row, columns=labels)

        price_pred = model.price_prediction(data)

    return render_template("homePage.html", predicted_price=price_pred)

if __name__ == "__main__":
    app.run(debug=True)
