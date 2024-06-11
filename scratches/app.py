from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Country data
countries = [
    {"name": "Germany", "code": "GER"},
    {"name": "France", "code": "FRA"},
    {"name": "Italy", "code": "ITA"},
    {"name": "Scotland", "code": "SCO"},
    {"name": "HUNGARY", "code": "HUN"},
    {"name": "SWITZERLAND", "code": "SUI"},
    {"name": "SPAIN", "code": "ESP"},
    {"name": "CROATIA", "code": "CRO"},
    {"name": "Albania", "code": "ALB"},
    {"name": "Slovenia", "code": "SVN"},
    {"name": "Denmark", "code": "DEN"},
    {"name": "Serbia", "code": "SRB"},
    {"name": "England", "code": "ENG"},
    {"name": "Draw", "code": "DRW"},
    # Add more countries here...
]

@app.route('/')
def index():
    return render_template('index.html', countries=countries)

#@app.route('/submit', methods=['POST'])

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    country = request.form['country']
    amount = int(request.form['amount'])

    # Define factors for each country
    country_factors = {
        "Germany": 1.5,
        "France": 1.8,
        "Italy": 1.7,
        # Add more countries and factors here...
    }

    factor = country_factors.get(country, 1.0)
    multiplied_amount = amount * factor

    with open('output.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, country, amount, multiplied_amount])

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
