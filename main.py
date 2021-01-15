
from flask import Flask, render_template
import requests
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
  data = get_current_state_data()
  return render_template("home.html", data=data)

@app.route('/map/')
def map_route():
    return render_template("map.html")
def get_current_state_data():
    response = requests.get("https://api.covidtracking.com/v1/states/current.json")
    remotedata = response.json()
    # data = []
    # for element in remotedata:
    #     data.append({ 'state': element['state'], 'positive': element['positive'], 'death': element['death']})

    # data = [
    #   { 'state': 'CA', 'positive': 2781039, 'death': 31102},
    #   { 'state': 'AZ', 'positive': 641729, 'death': 10673}
    # ]
    return remotedata

if __name__ == "__main__":
  #runs the application on the repl development server
  app.run(debug=True, port='3000', host='127.0.0.1')