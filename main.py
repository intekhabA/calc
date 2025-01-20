from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> intkehab alam flask api</h1>"

@app.route("/gratuity-calculator")
def gratuityCalculator():
    return render_template('gratuity-calculator.html')

@app.route('/percentage_calculator')
def percentageCalculator():
    return render_template('percentage_calculator.html')

@app.route('/salary_hike_percentage')
def salaryHikePercentage():
    return render_template('salary_hike_percentage.html')

if __name__ == "__main__":
    app.run(
        host='0.0.0.0', debug=True
    )