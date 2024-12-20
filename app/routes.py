from flask import Blueprint, jsonify, request, render_template
from app.calculations import calculate_fire, savings_needed

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')


@routes.route('/calculate', methods=['POST'])
def calculate():
    # Fetch and process input
    data = request.form
    current_portfolio = float(data['current_portfolio'])
    monthly_savings = float(data['monthly_savings'])
    fire_goal = float(data['fire_goal'])
    years = data.get('years', None)
    years = int(years) if years else None  # Convert to int if provided, else keep as None

    # Calculate results
    results = {
        "time_to_fire": calculate_fire(current_portfolio, fire_goal, monthly_savings),
        "savings_needed": savings_needed(current_portfolio, fire_goal, years)
    }
    return render_template('results.html', results=results)