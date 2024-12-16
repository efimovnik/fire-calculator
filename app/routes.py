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
    current_age = int(data['current_age'])
    current_portfolio = float(data['current_portfolio'])
    monthly_savings = float(data['monthly_savings'])
    fire_goal = float(data['fire_goal'])
    stocks_allocation = float(data['stocks_allocation'])
    years = data.get('years', None)
    years = int(years) if years else None  # Convert to int if provided, else keep as None

    # Calculate results
    if years:
        # If the user provides a target number of years, calculate savings needed
        required_savings = savings_needed(
            current_age, current_portfolio, fire_goal, years, stocks_allocation
        )
        results = {
            "required_monthly_savings": round(required_savings, 2),
            "years_provided": years
        }
    else:
        # If the user does not provide years, calculate time to FIRE and retirement age
        years_needed, retirement_age = calculate_fire(
            current_age, current_portfolio, fire_goal, monthly_savings, stocks_allocation
        )
        results = {
            "years_needed": years_needed,
            "retirement_age": retirement_age
        }

    # Render the results on a separate HTML page
    return render_template('results.html', results=results)
